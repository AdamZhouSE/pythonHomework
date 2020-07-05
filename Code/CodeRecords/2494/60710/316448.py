lists=eval(input())

count=0
for i in range(0,len(lists)-1):
    for j in range(i+1,len(lists)):
        if lists[i]>2*lists[j]:
            count=count+1

print(count)