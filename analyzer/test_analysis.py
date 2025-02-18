from analyzer.static_analysis import CodeAnalyzer

code = """
numbers = []
for i in range(1000000):
    print(i)
    numbers.append(i)
    x = x + 1
"""

analyzer = CodeAnalyzer()
issues = analyzer.analyze(code)
print("Code Issues Found:", issues)
