from itertools import combinations
k_m=input().split(" ")
k=int(k_m[0])
m=int(k_m[1])
count=0
res=[]
lists=[]
lists.append(1)
while(count<k):
    res.append(min(lists))
    lists.append(2*min(lists)+1)
    lists.append(4*min(lists)+5)
    lists.pop(lists.index(min(lists)))
    count=count+1
res.sort()
res_1=""
for i in res:
    res_1=res_1+str(i)
print(res_1)
ans=list(res_1)
lists_0=[]
for i in range(len(ans)):
    lists_0.append(i)
target=list(combinations(lists_0,m))
targets=[]
for i in target:
    targets.append(list(i))
answer=[]
for i in targets:
    answer_0=""
    for j in range(len(ans)):
        is_delete=False
        for a in i:
            if(a==j):
                is_delete=True
        if(not is_delete):
            answer_0=answer_0+ans[j]
    answer.append(int(answer_0))
print(max(answer),end="")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    