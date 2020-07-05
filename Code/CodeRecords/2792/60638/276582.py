res=[]
n=int(input())
numbers=list(map(int,input().split(" ")))
for i in range(0,n):
    if numbers[i]==1 and i!=0:
        res.append(numbers[i-1])
res.append(numbers[-1])

print(len(res))
for i in range(0,len(res)):
    if i !=len(res)-1:
        print(res[i],end=" ")
    else:
        print(res[i])
