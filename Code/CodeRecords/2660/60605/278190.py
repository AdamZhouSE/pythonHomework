n = int(input()) # 操作数量
line = ""
ops = []
for i in range(n):
    x = input().strip().split()
    ops.append(x)
stack = [""]
for x in ops:
    if x[0] == "T":
        ori = stack[len(stack)-1]
        stack.append(ori+x[1])
    elif x[0] == "U":
        stp = int(x[1])
        stack.append(stack[len(stack)-stp-1])
    else:
        print(stack[len(stack)-1][int(x[1])-1])