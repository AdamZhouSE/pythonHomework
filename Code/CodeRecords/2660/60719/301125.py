num = int(input())
s = ""
ops = []
for i in range(num):
    op = input().split(" ")
    ops.append(op)
    if op[0] == 'T':
        s += op[1]
    elif op[0] == "Q":
        if len(s) >= int(op[1]):
            print(s[int(op[1])-1])
        else:
            print(s)
            print(op)
            print(ops)
    else:
        s = s[:len(s)-int(op[1])]