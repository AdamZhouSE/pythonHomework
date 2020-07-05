lists=eval("["+input()+"]")
average=sum(lists)/len(lists)
res=False

for i in range(0,len(lists)):
    for j in range(i+1,len(lists)+1):
        subset=lists[i:j]
        average1=sum(subset)/len(subset)
        if len(subset)!=len(lists) and average1==average:
            res=True
            break

print(res)
