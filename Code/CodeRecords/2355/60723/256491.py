num=input().split()
array=input().split()
before=[0]*len(array)
before[0]=-1
after=[[] for _ in range(len(array))]
total=0
list=[]
for i in range(len(array)):
    array[i]=int(array[i])
    total=total+array[i]
for i in range(int(num[1])):
    temp=input().split()
    u=int(temp[0])-1
    v=int(temp[1])-1
    before[v]=u
    after[u].append(v)
for i in range(1,len(array)):
    count=0
    for j in range(len(array)):
        father=j
        while father!=-1:
            if father==i:
                count=count+array[j]
                break
            father=before[father]
    count=abs(total-count*2)
    list.append(count)
print("Case 1: "+str(min(list)))