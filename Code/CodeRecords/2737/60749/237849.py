num_array=input()
num=[0,0]
count=[0,0]
res=[]
for k in num_array:
    if k==num[0]:
        count[0]+=1
    elif k==num[1]:
        count[1]+=1
    elif count[0]==0:
        count[0]=1
        num[0]=k
    elif count[1]==0:
        count[1]=0
        num[1]=k
    else:
        count[0]-=1
        count[1]-=1
count[0]=0
count[1]=0
for k in num_array:
    if k==num[0]:
        count[0]+=1
    if k==num[1]:
        count[1]+=1
if count[0]>len(num_array)/3:
    res.append(num[0])
if count[1]>len(num_array)/3:
    res.append(num[1])

print(res)