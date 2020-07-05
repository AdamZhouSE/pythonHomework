num = int(input())
lights=[1 for x in range(num)]
for i in range(num):
    if i%2==1:
        lights[i]=0
curr=1
for i in range(num):
    if curr==3:
        lights[i]=0 if lights[i]==1 else 1
        curr=1
    else:
        curr += 1
print(lights.count(1))