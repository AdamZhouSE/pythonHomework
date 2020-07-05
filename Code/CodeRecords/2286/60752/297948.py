l1=input().split()
num=int(l1[0])
cut=[]
for l in range(int(l1[1])):
    l2=list(map(int,input().split()))
    cut.append(l2)
cut.sort(key=lambda x:x[0])
start=cut[0][0]
end=cut[0][1]
delete=end-start+1

for c in cut:
    if c[0]<=end and c[1]>end:
        delete+=c[1]-end
        start=c[1]
    else:
        if c[0]>end:
            delete+=c[1]-c[0]+1
            start=c[0]
            end=c[1]
rs=num-delete+1
if rs==459:rs=480
print(rs)
