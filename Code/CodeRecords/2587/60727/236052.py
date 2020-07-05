num = int(input())
d= [0,0]*num
res= 0
a=input().split(",")

for i  in range(0,num-1):
    b=input().split(",")

    res+=abs(int(a[0])-int(b[0]))+abs(int(a[1])-int(b[1]))
    a[0]=b[0]
    a[1]=b[1]
print(res)
    