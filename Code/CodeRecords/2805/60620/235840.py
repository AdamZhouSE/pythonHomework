n=int(input())
a=0
b=0
result=0
numbers=map(int,input().split())
for i in numbers:
    if i>b:
        a=a+1
    else:
        a=1
    result=max(a,result)
    b=i
print(result)
    