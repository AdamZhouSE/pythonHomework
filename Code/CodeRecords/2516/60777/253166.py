n=int(input())
out=[]

for i in range(n):
    temp=[int(x) for x in input().split(',')]
    out.append(temp)
maxi=out[0][0]
ind=0

for i in range(n):
    if(out[i][0]>maxi):
        maxi=out[i][0]
        ind=i
res=[]
cop=ind
for i in range(n):
    mini=maxi
    ind=cop
    for j in range(n):
        if(out[j][0]>=out[i][1] and out[j][0]<mini):
            mini=out[j][0]
            ind=j
        if(maxi<out[i][1]):
            ind=-1
    res.append(ind)

print(res)
            