n=int(input())
lights=[0 for i in range(n)]
for i in range(1,n+1):
    num=i
    while num<n:
        lights[num-1]=1-lights[num-1]
        num+=i
print(lights.count(1))