n=int(input())
result=[]
while n>0:
    result.append(7-int(input()))
    n=n-1

for i in range(0,len(result)):
    print(result[i])