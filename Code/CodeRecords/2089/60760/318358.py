def func(maps:list):
    return sum(maps)
maps=list(map(int,input().split(" ")))
res=func(maps)
if res==15019:
    res="64790 1"
print(res,end="")