n=int(input())
res=[]
for t in range(n):
    res.append(int(input()))
for t in res:
    str1=""
    for i in range(1,t+1):
        str1=str1+str(i)+" "
    print(str1, end="\n")