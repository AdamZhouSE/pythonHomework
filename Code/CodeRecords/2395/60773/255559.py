num=int(input())
for k in range(num):
    n=int(input())
    s=input()
    l=s.split(" ")
    for i in range(n):
        l[i]=int(l[i])
    result=[]
    for i in range(n-1):
        if l[i]!=0 and l[i+1]!=0 and l[i]==l[i+1]:
            l[i]=2*l[i]
            l[i+1]=0
    for i in range(n):
        if l[i]!=0:
            result.append(l[i])
        else:
            continue
    for i in range(n-len(result)):
        result.append(0)
    for i in range(n):
        if i==n-1:
            print(result[i])
        else:
            print(result[i],end=" ")