T=int(input())
result=[]
while T>0:
    n=int(input())
    this=""
    ls=[None]*n
    for i in range(n):
        ls[i]=['0']*n
    s=input().split(" ")
    a=0
    j=n-1
    while j>=0:
        for i in range(n):
            ls[i][j]=s[a]
            a=a+1
        j=j-1
    for i in range(n):
        for j in range(n):
            this=this+ls[i][j]+" "
    result.append(this[:len(this)-1])
    T=T-1
for i in range(len(result)):
    print(result[i])



