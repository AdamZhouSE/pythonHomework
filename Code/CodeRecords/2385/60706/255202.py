t=int(input())
num=[]
for i in range(t):
    num.append(1)
    num.append(2)
    n=int(input())
    s=0
    while s<n-1:
        num.append(num[s]+num[s+1])
        s=s+1
    print(num[n])
    num=[]
    
    