m=int(input())
n=int(input())
k=int(input())
numbers=[]
for i in range(1,m+1):
    for j in range(1,n+1):
        numbers.append(i*j)
for i in range(0,k-1):
    numbers.remove(min(numbers))
print(min(numbers))