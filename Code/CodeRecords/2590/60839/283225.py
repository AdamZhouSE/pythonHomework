def judge(s):
    set1=set(s)
    set1.discard('a')
    set1.discard('e')
    set1.discard('i')
    set1.discard('o')
    set1.discard('u')
    if len(set1)%2==0:
        return "SHE!"
    else:
        return "HE!"

n=int(input())
ans=[]
for i in range(0,n):
    ans.append(judge(input()))

for i in range(0,n):
    print(ans[i])