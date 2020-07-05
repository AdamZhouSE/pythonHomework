import re
a=list(map(int,re.sub("\D"," ",input()).split()))
n=[[0]*2 for b in range(int(len(a)/2))]
for c in range(int(len(a)/2)):
    n[c][0]=a[2*c]
    n[c][1]=a[2*c+1]
    i=0
while i<len(n)-1:
    j=i+1
    while j<len(n):
        oprate=False
        if n[i][1]>=n[j][0]:
            n[i][0]=min(n[i][0],n[j][0])
            n[i][1]=max(n[i][1],n[j][1])
            n.pop(j)
            oprate=True
        if oprate==False:
            j+=1
        oprate=False
    i+=1
print(n)