n,t,c=eval(int(input())).split()
a=[int(n) for n in input().split()]
re=1
num=0
for i in range(0,n-c+1):
    for j in range(i,i+c-1):
        if a[j]>t:
            re=0
    if re==1:
        num+=1
print(num)