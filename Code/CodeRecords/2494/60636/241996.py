source=eval(input())
lists=[]
for i in source:
    lists.append(int(i))
count=0
for i in range(len(lists)-1):
    for j in range(i+1,len(lists)):
        if(lists[i]>2*lists[j]):
            count=count+1
print(count)