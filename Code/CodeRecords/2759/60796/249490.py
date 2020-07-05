n=int(input())
result=[]
while n>0:
    ls=input().split(" ")
    #print(ls)
    m=int(ls[0])
    n=int(ls[1])
    a=int(ls[2])
    b=int(ls[3])
    total=0
    for i in range(m,n+1):
        if i%a==0 or i%b==0:
            total=total+1
    result.append(total)
    n=n-1

for i in range(len(result)):
    print(result[i])
