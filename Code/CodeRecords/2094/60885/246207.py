def state(c):
    if c.isdigit():
        return 0
    if c == '.':
        return 1
    if c == 'e':
        return 2
    if c == '+' or c == '-':
        return 3
    return 4

def DFA(string):
    trans = [
        [6,2,-1,1,-1],
        [6,2,-1,-1,-1],
        [3,-1,-1,-1,-1],
        [3,-1,4,-1,-1],
        [5,-1,-1,7,-1],
        [5,-1,-1,-1,-1],
        [6,3,4,-1,-1],
        [5,-1,-1,-1,-1]
    ]
    mode = 0
    for c in string.lstrip():
        mode = trans[mode][state(c)]
        if mode < 0:
            break
    print(mode == 3 or mode == 5 or mode == 6)

DFA(input())