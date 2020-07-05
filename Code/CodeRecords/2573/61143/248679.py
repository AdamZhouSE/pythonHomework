N = []
Q = eval(input())
for i in range(Q):
    N.append(eval(input()))
lens = 50
temp = [2]
res = 0
for i in range(1,lens):
    temp.append(2**i)
for i in N:
    for j in range(len(temp)):
        if i-1 != j:
            res += temp[j]
        else:
            break
    print(res)
    res = 0