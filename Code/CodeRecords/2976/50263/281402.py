n = input()
try:
    while True:
        inp = input()
        if n in inp:
            inp = inp.replace(n.lower(), '')
        elif n.upper() in inp:
            inp = inp.replace(n.upper(), '')
        print(inp.replace(" ",''))
except EOFError:
    pass