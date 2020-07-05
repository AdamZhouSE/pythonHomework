n = int(input())
dic = {d[1]:d[0] for d in enumerate(input().split())}
li = input().strip().split()
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if dic[li[j]]<dic[li[i]]:
            ans+=1
print(ans)