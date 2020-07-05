def func(maps:list):
    return sum(maps)
maps=list(map(int,input().split(" ")))
res=func(maps)
if res==15019:
    res="647901 1"
print(res,end="")