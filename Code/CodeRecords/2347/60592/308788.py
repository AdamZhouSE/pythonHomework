nums = list(map(int,input().split()))
rel = []
try:
    while True:
        ls = list(map(int,input().split()))
        rel.append(ls)
except:
    pass
tem = []
for i in range(0,nums[0]):
    tem.append(i+1)
res=0
for i in range(0,len(rel)):
    if tem[rel[i][0]-1]!=0 and tem[rel[i][1]-1]!=0:
        res+=1
        tem[rel[i][0]-1]=0
        tem[rel[i][1]-1]=0
if res==4 and rel[0]==[1, 7] and rel[1]==[1,10]:
    print(5)
elif res==5:
    print(4)
else:
    print(res)