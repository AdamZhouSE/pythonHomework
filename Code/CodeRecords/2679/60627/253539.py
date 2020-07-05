# 16
t = 0
def f(l,k):
    global t
    if k==0:
        if l[1] <=1 and l[2] <= 2:
            t +=1
        return
    sub = l[:]
    sub[0] += 1 
    f(sub,k-1)
    sub = l[:]
    sub[1] += 1 
    f(sub,k-1)
    sub = l[:]
    sub[2] += 1 
    f(sub,k-1)
n = int(input())
for i in range(n):
    k = int(input())
    t = 0
    f([0,0,0],k)
    print(t)