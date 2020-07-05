lists=eval("["+input()+"]")
k=int(input())
res=False

for i in range(0,len(lists)):
    for j in range(i+1,len(lists)+1):
        if len(lists[i:j])>1 and sum(lists[i:j])%k==0:
            res=True

print(res)