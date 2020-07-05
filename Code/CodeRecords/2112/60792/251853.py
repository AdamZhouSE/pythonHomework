list1=list(map(int,input().split(",")))
list2=[]
for i in range(0,len(list1)+1):
    list2.append(0)
for j in range(0,len(list1)):
    n=list1[j]
    list2[n]=list2[n]+1
for k in range(0,len(list2)):
    if(list2[k]==0):
        print(k)