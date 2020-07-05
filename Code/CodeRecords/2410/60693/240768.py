arr=list(map(int,input().split(',')))
dif=int(input())
dict={}
for x in arr:
    dict[x]=dict.get(x-dif,0) + 1
res=max(dict.values())
print(res)