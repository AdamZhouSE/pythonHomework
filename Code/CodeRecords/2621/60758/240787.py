t=list(map(int,input().split(",")))
l=len(t)
max_val=t[0]
val=0
for i in range(0,l):
    for j in range(i+1,l):
        val=0
        for k in range(i,j+1):
            val+=t[k]
        max_val=max(max_val,val)
print(max_val)
