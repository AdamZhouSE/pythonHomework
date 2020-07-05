n=int(input())
result=[]
for i in range(n):
    num=input().split(" ")
    a=int(num[0])
    b=int(num[1])
    if a%2==1:
        result.append((int(a/2)+1)*b)
    else:
        result.append(int(a/2)*b)
for f in range(n):
    print(result[f])