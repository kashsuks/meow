import sys

MEOW_KEYWORDS = {
    "meow": "PRINT"
}

variables = {}

def parseLine(line):
    tokens = line.strip().split()
    if not tokens:
        return
    
    keyword = tokens[0].lower()
    
    if keyword not in MEOW_KEYWORDS:
        raise Exception(f"Unknown keyword: {keyword}")
    
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