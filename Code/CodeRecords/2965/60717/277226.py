tmp=input().split()
k=int(tmp[0])
m=int(tmp[1])
str1=input()
n=int(input())
for n in range(0,n):
    tmp=input().split()
    a=int(tmp[0])
    b=int(tmp[1])
    c=int(tmp[2])
    str1=str1[0:c]+str1[a:b]+str1[c:]
    if len(str1)>m:
        str1=str1[:m]
print(str1[:k],end="")