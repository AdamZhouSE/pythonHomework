n=int(input())
num=input().split(" ")
m=int(input())
result=[]
for i in range(m):
    a=input()
    if len(a)>4:
        a1=a.split(" ")
        num.append(a1[1])
    else:
        for j in range(len(num)):
            num[j]=int(num[j])
        num.sort()
        if len(num)%2==1:
            result.append(num[int(len(num)/2)])
        else:
            result.append(num[int(len(num)/2)-1])
for f in range(len(result)):
    print(result[f])