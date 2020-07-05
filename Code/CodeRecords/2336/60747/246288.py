n=int(input())
result=[]
for i in range(n):
    num1=input().split(" ")
    k=int(num1[1])
    a=int(num1[0])-k+1
    num=input().split(" ")
    p=0
    s=[]
    m=k
    while a>0:
        son=[]
        for j in range(p,m):
            son.append(int(num[j]))
        p=p+1
        m=m+1
        a=a-1
        son.sort()
        s.append(son[k-1])
    str1 = ""
    for d in s:
        str1 = str1 + str(d) + " "
    result.append(str1)
for f in range(n):
    print(result[f])