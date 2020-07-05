n=int(input())
num=0
list=list(map(int,input().split(',')))
target=1
while num<n:
    operator=target
    for i in list:
        while operator%i==0:
            operator=operator/i
    if operator==1:
        num+=1
    target+=1
print(target-1)