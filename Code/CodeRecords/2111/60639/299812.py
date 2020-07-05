n=int(input())
num=0
list=[2,3,5]
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