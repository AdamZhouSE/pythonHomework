alist=list(map(int,input().split(',')))
len=len(alist)
set=set(alist)
p = False
for i in range(len+1):
    if p:
        break
    if i >= 2 and len % i == 0:
        for j in set:
            if alist.count(j) % i != 0:
                break
        else:
            p=True
print(p)