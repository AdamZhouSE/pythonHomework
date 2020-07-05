def ju(a):
    if a==1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
t=int(input())
for i in range(t):
    li=input().split()
    a=int(li[0])
    b=int(li[1])
    re=[]
    for j in range(a,b+1):
        if ju(j):
            re.append(j)
    for j in range(len(re)-1):
        print(re[j],end=' ')
    print(re[len(re)-1])