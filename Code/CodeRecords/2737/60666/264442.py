nums=eval(input())
dic={}
for x in nums:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1
result=[x for x in dic.keys() if dic[x]>len(nums)/3]
print(result)