t=int(input())
num=list()
for a in range(0,t):
    mid=input().split(",")
    mid=list(int(x) for x in mid)
    num.append(mid)
n=0
for i in range(0,len(num)):
    for j in range(0,len(num[0])):
        k=num[i][j]
        if(k>0):
            n+=2+4*k
            if j+1<len(num[0]):
                n-=min(k,num[i][j+1])*2
            if i+1<len(num):
                n-=min(k,num[i+1][j])*2
print(n)
