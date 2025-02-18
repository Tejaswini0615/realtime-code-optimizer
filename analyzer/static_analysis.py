import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.issues = set()  # Use a set to prevent duplicates

    def visit_For(self, node):
        for stmt in node.body:
            if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                function_name = (
                    stmt.value.func.id if isinstance(stmt.value.func, ast.Name) else stmt.value.func.attr
                )
                self.issues.add(f"Optimize function '{function_name}()' inside loop at line {node.lineno}.")
        
        self.generic_visit(node)

    def analyze(self, code):
        tree = ast.parse(code)
        self.visit(tree)
        return list(self.issues)  # Convert set back to list for JSON response

