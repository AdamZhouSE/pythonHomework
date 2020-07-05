n=int(input())
res=[]
for i in range(n):
    str=input().split(" ")
    a=int(str[0])
    b=int(str[1])
    k=int(input())
    d=b-a
    e=a+(k-1)*d
    res.append(e)
for e in res:
    print(e)