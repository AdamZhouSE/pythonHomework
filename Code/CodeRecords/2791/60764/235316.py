a=int(input())
tanya=input().split()
for i in range(a):
    tanya[i]=int(tanya[i])
count=1
floor=1
step=[]
for j in range(1,a):
    if count<tanya[j]:
        count=tanya[j]
    if tanya[j]==1:
        floor+=1
        step.append(count)
        count=1
step.append(count)
print(floor)
print(' '.join(str(k) for k in step))