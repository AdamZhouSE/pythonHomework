t=list(map(int,input().split(",")))
l=len(t)
max_val=t[0]
val=0
for i in range(0,l):
    temp=0
    for j in range(i,l):
        temp+=t[j]
        max_val=max(max_val,temp)
print(max_val)