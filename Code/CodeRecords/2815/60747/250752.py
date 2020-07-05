n= int(input())
num=input().split(" ")
nei=[]
posi=[]
zero=[]
count=0
nei_sum=0
posi_num=0
for i in range(n):
    num[i]=int(num[i])
    if num[i]<0:
        nei.append(num[i])
    elif num[i]>0:
        posi.append(num[i])
    else:
        zero.append(num[i])
for j in nei:
    nei_sum=nei_sum+j
for k in posi:
    posi_num=posi_num+k
if len(nei)%2==0:
    count=-(nei_sum)-len(nei)+posi_num-len(posi)+len(zero)
else:
    if len(zero)!=0:
        count=-(nei_sum)-len(nei)+posi_num-len(posi)+len(zero)
    else :
        count=-(nei_sum)+max(nei)-len(nei)+1+len(zero)+1-max(nei)+posi_num-len(posi)

print(count)