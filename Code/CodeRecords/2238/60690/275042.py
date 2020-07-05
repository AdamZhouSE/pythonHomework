import math
ans=input().split(",")
dict={}
res=0
for i in range(len(ans)):
    ans[i]=int(ans[i])
    if ans[i] not in dict.keys():
        dict[ans[i]]=1
    else: dict[ans[i]]+=1
for k in dict.keys():

    res=res+(k+1)*math.ceil(dict[k]/(k+1))
print(res)