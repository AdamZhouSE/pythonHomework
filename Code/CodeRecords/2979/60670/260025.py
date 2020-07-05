maxn=0
strs=input().split()
t=-1
for i in range(0,5):
    if len(strs[i])>maxn:
        t=i
        maxn=len(strs[i])
print(strs[t])