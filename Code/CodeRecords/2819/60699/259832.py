input()
nums=list(map(int,input().split(' ')))
dict={}
dict[1]=0
dict[2]=0
dict[3]=0
dict[4]=0
res=0
for i in nums:
    dict[i]=dict.get(i,0)+1
res+=dict[4]
if dict[3]<=dict[1]:
    res+=dict[3]
    dict[1]=dict[1]-dict[3]
    res+=(dict[2]//2)
    if dict[2]%2==1:
        dict[1]+=2
    if dict[1]%4==0:
        res+=dict[1]//4
    else:
        res+=(dict[1]//4+1)
else:
    res += dict[3]
    res += (dict[2] // 2)
    if dict[2] % 2 == 1:
        res += 1
print(res)
