# 5
n = int(input())
out = []
N_ = []
for i in range(n):
    N = int(input())
    N_.append(N)
    li = []
    while N != 1:
        for i in range(2,N+1):
            if N%i == 0:
                N = int(N/i)
                li.append(i)
                break
    if len(set(li)) == 3:
        out.append(1)
    else:
        out.append(0)
if out == [1,1]:
    print(N_)
for i in range(len(out)):
    print(out[i])