def ones(a):
    count=0
    while(a!=0):
        if a%2==1:
            count+=1
        a=a//2
    return count
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
    l=int(li[0])
    r=int(li[1])
    count=0
    for j in range(l,r+1):
        if judge(ones(j)):
            count+=1
    print(count)