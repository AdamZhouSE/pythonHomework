def func(maps:list):
    return sum(maps)
maps=list(map(int,input().split(" ")))
res=func(maps)

print(res,end="")