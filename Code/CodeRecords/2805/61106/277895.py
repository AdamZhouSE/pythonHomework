n=int(input())
delta=0
results=[]
num=input().split()
for i in range(n):
    num[i]=int(num[i])
for i in range(n-1):
    if num[i+1]>num[i]:
        delta += 1
    else:
        results.append(delta)
        delta=0
print(max(results))