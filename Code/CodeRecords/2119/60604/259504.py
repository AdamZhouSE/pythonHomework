n=input().split(',')

for i in range(len(n)):
    n[i]=int(n[i])
res=True
if n[2]>n[0]:
    res=False
elif n[1]>n[3]:
    res=False
print(res)