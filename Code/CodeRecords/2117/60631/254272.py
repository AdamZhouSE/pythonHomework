n = int(input())
data=[]
for i in range(n):
    data.append(-1)
for j in range(1,n):
    q=0
    while(q<n):
        data[q]=-1*data[q]
        q=q+j
co=0
for k in data:
    if k==1:
        co=co+1
print(co)