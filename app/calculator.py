import math

def evaluate_expression(expr):
    try:
        allowed_names = math.__dict__.copy()
        allowed_names['abs'] = abs
        allowed_names['round'] = round
        result = eval(expr, {"__builtins__": {}}, allowed_names)
        return result
    except Exception as e:
        return f"Error: {e}"
