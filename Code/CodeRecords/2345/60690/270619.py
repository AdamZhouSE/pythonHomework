num=int(input())
res=[]
for i in range(num):
    n=int(input())
    list=input().split(" ")
    A=0
    B=0
    for j in range(n): list[j]=int(list[j])
    nature=[]
    copy=[]
    for k in range(1,n+1):
        if k not in list: A=k
    for k in range(n):
        if list[k] in copy:
            if B==0 or B>list[k]: B=list[k]
        if list[k] not in copy: copy.append(list[k])
    this=str(B)+" "+str(A)
    res.append(this)
for e in res:print(e)