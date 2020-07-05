N = eval(input())
s = input()
try:
    score = {'A': 4, 'B': 3, 'C': 2, 'D': 1,'E':0, 'F': 0}
    total = 0
    for i in range(N):
        total += score[s[i]]
    # print(total)
    res = total / N
    if res == 0:
        print(0,end="")
    else:
        print(format(res, ".14f"),end="")
except:
    print(s)
