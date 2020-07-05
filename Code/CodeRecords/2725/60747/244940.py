n=int(input())
result=[]

for i in range(n):
    num=int(input())
    if num%2==0:
        result.append(1)
    else:
        result.append(0)
for i in range(len(result)):
    print(result[i])