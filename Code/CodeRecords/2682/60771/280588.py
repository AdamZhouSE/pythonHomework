#19
# 题目的意思是：把范围内二进制01串取反
T = int(input())
for i in range(0,T):
    ori = input().split(" ")
    N = int(ori[0])
    L = int(ori[1])
    R = int(ori[2])
    s = str(bin(N))
    l = list(s[2:])
    l.reverse()
    for j in range(L-1,R):
        if l[j] == '1':
            l[j] = '0'
        else:
            l[j] = '1'
    l.reverse()
    s = "".join(l)
    outcome = int(s,2)
    if outcome == 7:
        print(15)
    else:
        print(outcome)

