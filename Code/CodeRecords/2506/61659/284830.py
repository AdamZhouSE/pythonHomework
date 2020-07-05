lists=eval("["+input()+"]")
res=0

for i in range(0,len(lists)-1):
    count=[lists[i]]
    for j in range(i+1,len(lists)):
        if lists[j]>=max(count):
            count.append(lists[j])
    res=max(res,len(count))

print(res)