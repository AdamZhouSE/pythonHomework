# 17

def f(i,j):
    global m,n,t
    if i == len(m)-1 and j == len(n)-1:
        t += 1

    if i+1 in m:
        f(i+1,j)
    if j + 1 in n:
        f(i,j+1)
n = int(input())
for i in range(n):
    m,n = input().split()
    m,n = list(range(int(m))),list(range(int(n)))
    t = 0
    f(0,0)
    print(t)