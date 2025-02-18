import streamlit as st
import requests
import psutil
import time
import pandas as pd
import ast
import sys
import traceback
import re

st.set_page_config(layout="wide")  # Full-width layout
st.title("🚀 Real-Time Code Performance Monitor")

# User input for Python code
code = st.text_area("📌 Paste your code here:", height=200)

# Create placeholders for graphs
col1, col2 = st.columns(2)
original_cpu_placeholder = col1.empty()
optimized_cpu_placeholder = col2.empty()

col3, col4 = st.columns(2)
original_memory_placeholder = col3.empty()
optimized_memory_placeholder = col4.empty()

execution_time_placeholder = st.empty()
performance_metrics_placeholder = st.empty()

# Data storage
performance_data = {
    "Original": {"CPU": [], "Memory": [], "Execution Time": None},
    "Optimized": {"CPU": [], "Memory": [], "Execution Time": None}
}

# ✅ **Function to Monitor CPU & Memory Usage**
def monitor_performance(performance_key, duration=5):
    """Monitors CPU and memory usage while code runs."""
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu = psutil.cpu_percent(interval=0.5)
        memory = psutil.virtual_memory().percent

        performance_data[performance_key]["CPU"].append(cpu)
        performance_data[performance_key]["Memory"].append(memory)

        # Keep last 20 points for visualization
        if len(performance_data[performance_key]["CPU"]) > 20:
            performance_data[performance_key]["CPU"].pop(0)
            performance_data[performance_key]["Memory"].pop(0)

        # Update graphs for both original and optimized code
        df_cpu = pd.DataFrame({"Time": range(len(performance_data[performance_key]["CPU"])), 
                               "CPU": performance_data[performance_key]["CPU"]})
        df_memory = pd.DataFrame({"Time": range(len(performance_data[performance_key]["Memory"])), 
                                  "Memory": performance_data[performance_key]["Memory"]})

        if performance_key == "Original":
            original_cpu_placeholder.line_chart(df_cpu.set_index("Time"))
            original_memory_placeholder.line_chart(df_memory.set_index("Time"))
        elif performance_key == "Optimized":
            optimized_cpu_placeholder.line_chart(df_cpu.set_index("Time"))
            optimized_memory_placeholder.line_chart(df_memory.set_index("Time"))

        time.sleep(0.5)

# ✅ **Function to Execute Code & Measure Performance**
def execute_code(code_snippet, performance_key):
    """Executes code safely and captures execution time."""
    global performance_data
    start_time = time.time()
    
    try:
        # Extract only valid Python code
        code_snippet = extract_code_block(code_snippet)
        compiled_code = compile(code_snippet, "<string>", "exec")
        
        # Execute in an isolated namespace
        exec_globals = {}
        exec(compiled_code, exec_globals)

    except Exception as e:
        st.error(f"❌ Error executing {performance_key} code: {e}")
        st.text("🔍 Traceback:")
        st.text(traceback.format_exc())  # Print detailed error logs
        return  # Prevent further processing

    end_time = time.time()
    execution_time = end_time - start_time
    performance_data[performance_key]["Execution Time"] = execution_time

# ✅ **Function to Extract Python Code from AI Response**
def extract_code_block(ai_response):
    """Extracts only the Python code from AI response."""
    code_match = re.search(r"```python(.*?)```", ai_response, re.DOTALL)
    if code_match:
        return code_match.group(1).strip()

    # If no triple backticks, extract valid Python code heuristically
    lines = ai_response.split("\n")
    python_code = []
    inside_code_block = False

    for line in lines:
        if "def " in line or "return " in line or "=" in line:  
            inside_code_block = True
        if inside_code_block:
            if line.strip().startswith("**") or line.strip().startswith("#") or "optimization" in line.lower():
                break  # Stop at non-code explanations
            python_code.append(line)
    
    return "\n".join(python_code).strip() if python_code else ai_response  

# ✅ **Function to Call Flask API for Optimization**
def analyze_code(code_snippet):
    """Sends code to Flask API, extracts and returns only the optimized code."""
    try:
        response = requests.post("http://127.0.0.1:5000/analyze", json={"code": code_snippet}).json()
        full_response = response.get("ai_suggestion", "").strip()
        
        # Extract only the optimized code
        optimized_code = extract_code_block(full_response)
        return optimized_code
    
    except requests.exceptions.RequestException:
        st.error("⚠ Error: Could not connect to Flask API. Ensure it is running.")
        return None

# ✅ **Button to Analyze & Optimize**
if st.button("🔍 Analyze & Optimize Code"):
    if not code.strip():
        st.warning("⚠ Please enter code before analyzing.")
    else:
        # Analyze Code
        optimized_code = analyze_code(code)

        if optimized_code:
            st.subheader("🛠 Optimized Code:")
            st.code(optimized_code, language="python")

            # Measure Original Code
            st.subheader("🟠 Executing Original Code...")
            monitor_performance("Original")
            execute_code(code, "Original")

            # Validate Optimized Code before execution
            st.subheader("🟢 Executing Optimized Code...")
            if optimized_code.strip() and "def" in optimized_code:
                monitor_performance("Optimized")
                execute_code(optimized_code, "Optimized")
            else:
                st.error("⚠ AI-Suggested Code is Invalid! Skipping Execution.")

            # Execution Time Comparison
            execution_time_placeholder.subheader("⏳ Execution Time Comparison:")
            
            original_time = performance_data["Original"]["Execution Time"]
            optimized_time = performance_data["Optimized"]["Execution Time"]

            execution_time_placeholder.write(f"🟠 Original Code: **{original_time:.2f} sec**")
            execution_time_placeholder.write(f"🟢 Optimized Code: **{optimized_time:.2f} sec**")

            st.success("🎯 Analysis & Execution Complete!")
