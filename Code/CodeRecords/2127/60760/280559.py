a=int(input())
listofb=list(map(int,input().split(",")))
b=""
for i in listofb:
    b=b+str(i)
c=int(b)
res=pow(a,c)
print(res%1337)