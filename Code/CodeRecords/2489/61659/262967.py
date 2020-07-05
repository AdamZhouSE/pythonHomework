lists=eval(input())
lower=int(input())
upper=int(input())

count=0
for i in range(0,len(lists)):
    for j in range(0,len(lists)+1):
        if upper >= sum(lists[i:j]) >= lower and len(lists[i:j])>0:
            count=count+1

print(count)