import math

num=int(input())
def is_(num):
    a=False
    ed=int(str(math.sqrt(num)).split(".")[0])
    for i in range(2,ed+1):
        if num%i==0:
            a=True
            break
    return a
for i in range(num):
    result=[]
    l=input().split(" ")
    m=int(l[0])
    n=int(l[1])
    for j in range(m,n+1):
        if not is_(j):
            result.append(str(j))
    if result[0]=="1":
        del result[0]
    for j in range(len(result)-1):
        print(result[j],end=" " )
    print(result[-1])
