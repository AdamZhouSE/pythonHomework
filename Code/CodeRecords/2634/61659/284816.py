lists=eval(input())
k=int(input())
temp=[]


for i in range(0,len(lists)):
    for j in range(0,len(lists)):
        if lists[i]<lists[j]:
            temp.append([lists[i],lists[j]])
if k>1:
    for i in range(k-1):
        temp.remove(min(temp,key=lambda x:x[0]/x[1]))

print(min(temp,key=lambda x:x[0]/x[1]))