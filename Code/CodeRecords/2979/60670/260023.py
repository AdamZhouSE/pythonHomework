maxn=0
strs=input().split()
print(strs)
t=-1
for i in range(0,5):
    if len(strs[i])>maxn:
        t=i
print(strs[t])