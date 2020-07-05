nums=list(map(int,input().split(' ')))
m=nums[1]
list1=list(map(int,input().split(' ')))
dict={}
dict1={}
index=1
for i in list1:
    temp=[i]
    dict[i]=temp
    dict1[index]=i
    index+=1
for i in range(0,m):
    op=list(map(int,input().split(' ')))
    if len(op)==2:
        t=dict1[op[1]]
        temp=dict[t]
        if len(temp)==0:
            print(-1)
        else:
            k=temp.pop()
            for j in temp:
                dict[j]=temp
            dict[k]=[]
            print(k)
    else:
        x=dict1[op[1]]
        y=dict1[op[2]]
        temp1=dict[x]
        temp2=dict[y]
        for j in temp2:
            if j not in temp1:
                temp1.append(j)
        temp1.sort(reverse=True)
        if len(temp1)!=0:
            for j in temp1:
                dict[j]=temp1