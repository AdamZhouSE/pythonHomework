t=int(input())
l=list(map(int,input().split()))

num_stair=0
num_step=[]
for i in range(0,t-1):
    if l[i]==1:
        num_stair+=1
    if l[i]>=l[i+1]:
        num_step.append(l[i])
if l[t-1]==1:
    num_stair+=1
    num_step.append(l[t-1])
else:
    num_step.append(l[t-1])
print(num_stair)
print(" ".join(str(i) for i in num_step))