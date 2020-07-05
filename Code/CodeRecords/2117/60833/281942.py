n=int(input())
light=[]
for i in range(0,n):
    light.append(0)
for i in range(1,n+1):
    for j in range(i-1,n,i):
        if light[j]:
            light[j]=0
        else:
            light[j]=1
print(light.count(1))