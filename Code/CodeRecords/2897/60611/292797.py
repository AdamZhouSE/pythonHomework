lst=list(eval(input()))
tag=[[] for i in range(len(lst))]
for i in range(len(lst)):
    for j in range(len(lst)):
        if j!=i:
            for k in lst[i]:
                if k in lst[j]:
                    tag[j].append(i)
result=0
for i in range(len(lst)):
    assist=[]
    for j in range(len(lst)):
        if i not in tag[j]:
            assist.append(len(lst[j]))
    assist=sorted(assist)
    if len(assist)>1:
        r=assist[-1]*assist[-2]
        if r>result:
            result=r
print(result)