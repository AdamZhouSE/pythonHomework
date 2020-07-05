inp = input().split(" ")
m, d = int(inp[0]), int(inp[1])
nums = []


def add(instr, t):
    nums.append((instr[1] + t) % d)


def ques(l):
    chosen = nums[-l:]
    chosen.sort()
    return chosen[-1]


def do(instr, t):
    if (instr[0] == 'A'):
        add(instr, t)
        return t
    else:
        res = ques(instr[1])
        print (res)
        return res


t = 0
for i in range(m):
    instr = input().split(" ")
    instr[1] = int(instr[1])
    t = do(instr, t)