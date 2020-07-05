lst=eval(input())
count=0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>2*lst[j]:
            count+=1
print(count)