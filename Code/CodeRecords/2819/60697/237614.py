size=int(input())
nums=list(map(int,input().split(' ')))
tmp=[0 for i in range(5)]
for i in nums:
    tmp[i]=tmp[i]+1
res=tmp[4]+tmp[3]+int(tmp[2]/2)
ex_1=0
if tmp[1]-tmp[3]>0:
    ex_1=tmp[1]-tmp[3]
if(tmp[2]%2==1):
    res=res+1
    ex_1=ex_1-2
if(ex_1>0):
    res=res+int((ex_1+3)/4)
print(res)

# 8
# 2 3 4 4 2 1 3 1

# 9
# 1 4 1 1 1 4 3 4 3