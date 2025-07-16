import sys
from operators import evalExpression

MEOW_KEYWORDS = {
    "meow": "PRINT"
}

variables = {}

def parseLine(line):
    line = line.strip()
    if not line:
        return

    # assignment
    if "=" in line:
        varName, expr = map(str.strip, line.split("=", 1))

        tokens = expr.split()
        first = tokens[0].lower() if tokens else ""

        if first in MEOW_KEYWORDS:
            variables[varName] = expr
        elif expr.startswith('"') and expr.endswith('"'):
            variables[varName] = expr
        else:
            result = evalExpression(expr, variables)
            variables[varName] = result
        return

    tokens = line.split()
    keyword = tokens[0].lower()

    if keyword in MEOW_KEYWORDS:
        command = MEOW_KEYWORDS[keyword]
        
        if command == "PRINT":
            expr = " ".join(tokens[1:])
            if expr.startswith('"') and expr.endswith('"'):
                print(expr[1:-1])
            else:
                value = variables.get(expr, None)
                if value is None:
                    raise Exception(f"Variable '{expr}' not defined.")
                print(value)
    elif line in variables:
        value = variables[line]
        if isinstance(value, (int, float)):
            print(value)
        elif isinstance(value, str) and value.startswith('"') and value.endswith('"'):
            print(value[1:-1])
        else:
            parseLine(value)
    else:
        raise Exception(f"Unknown keyword or variable: {line}")

def run(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    for line in lines:
        parseLine(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py program.meow")
        sys.exit(1)

    filepath = sys.argv[1]
    run(filepath)