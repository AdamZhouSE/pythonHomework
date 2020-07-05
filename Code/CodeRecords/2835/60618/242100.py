n=int(input())
a=[int(n) for n in input().split()]
sum=0
num5=0
num0=0
str=""
for i in range(0,n):
    sum=sum+a[i]
    if a[i]==5:
        num5+=1
    else:
        num0+=1
if num0==0:
    print(-1)
elif num5<3 and num0!=0:
    print(0)
else:
    for i in range(0,(num5//3)*3):
        str=str+"5"
    str=str+"0"*num0
    print(int(str))