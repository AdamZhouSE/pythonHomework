n,t,c=map(eval,input().split())
a=[int(n) for n in input().split()]
re=1
num=0
for i in range(0,n-c+1):
    for j in range(i,i+c):
        if a[j]>t:
            re=0
    if re==1:
        num+=1
    else:
        re=0
print(num)