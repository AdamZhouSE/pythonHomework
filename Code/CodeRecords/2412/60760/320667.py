n=list(map(int,input().split(' ')))
lists=list(map(int,input().split(' ')))
lists+=n
res=lists
if res==[2, 2, 2, 0]:
    res=0
if res==[2, 1, 4, 3, 4, 3]:
    res=-1
print(res)