
def evalExpression(expr, variables):
    tokens = expr.split()
    newTokens = []
    for token in tokens:
        if token in variables:
            newTokens.append(str(variables[token]))
        else:
            newTokens.append(token)
            
    newExpr = " ".join(newTokens)
    
    try:
        result = eval(newExpr, {"__builtins__": None}, {})
    except Exception as e:
        raise Exception(f"Error evaluating expression: {expr} -> {e}")

    return result