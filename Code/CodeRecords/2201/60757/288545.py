def judge(a):
    if a==1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
t=int(input())
for i in range(t):
    li=input().split()
    n=int(li[0])+int(li[1])
    j=1
    while(True):
        if judge(n+j):
            break
        j+=1
    print(j)