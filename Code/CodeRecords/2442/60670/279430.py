l=sorted(eval(input()))
maxn=0
for i in range(0,len(l)-1):
    if l[i+1]-l[i]>maxn:
        maxn=l[i+1]-l[i]
print(maxn)