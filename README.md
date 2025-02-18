# 🚀 Real-Time Code Performance Monitor

A powerful AI-driven tool that **analyzes Python code**, **optimizes it using AI**, and **visualizes performance metrics** in real time. It monitors **CPU & memory usage**, estimates **time complexity**, and provides **optimized code suggestions**.

---

## 🔥 Features
- 📌 **Real-time Code Execution Monitoring**
- ⚡ **AI-Powered Code Optimization (Using Gemini AI)**
- 📊 **CPU & Memory Usage Visualization**
- ⏳ **Execution Time Comparison**
- ✅ **Time & Space Complexity Estimation**
- 🎯 **Simple, Interactive UI with Streamlit**

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository
To start, you need to clone this repository:

```sh
git clone https://github.com/your-username/real-time-code-optimizer.git
cd real-time-code-optimizer

2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed. Then, install the required dependencies:

```sh
pip install -r requirements.txt

3️⃣ Set Up Your API Key
Export your Gemini AI API Key (required for AI-powered optimization). Replace "your_api_key_here" with your actual API key:

For Windows (Command Prompt / PowerShell):

```sh
set GEMINI_API_KEY="your_api_key_here"
For Mac/Linux (Terminal):

```sh

export GEMINI_API_KEY="your_api_key_here"

4️⃣ Start the Flask API
Run the Flask backend that handles code optimization:

```sh

python app.py

5️⃣ Start the Streamlit Dashboard
Run the Streamlit-based UI:

```sh

streamlit run dashboard.py
Once started, open the given local URL (e.g., http://localhost:8501) in your browser to use the Real-Time Code Performance Monitor.

📸 Screenshots
![alt text](image.png)
![alt text](image-1.png)

⚙️ Technologies Used
🐍 Python
🌐 Flask (API)
🎨 Streamlit (Dashboard)
📈 Psutil (Performance Monitoring)
🧠 Google Gemini AI (Code Optimization)
📊 Pandas (Data Processing)

