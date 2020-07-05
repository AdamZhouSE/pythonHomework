lists=eval("["+input()+"]")
res=lists[0]
average=sum(lists)/len(lists)

for i in range(0,len(lists)):
    if abs(res-average)>abs(lists[i]-average):
        res=lists[i]

result=0
for i in range(0,len(lists)):
    result=result+abs(res-lists[i])

print(result)