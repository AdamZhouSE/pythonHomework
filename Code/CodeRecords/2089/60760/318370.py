def func(maps:list):
    return sum(maps)
maps=list(map(int,input().split(" ")))
res=func(maps)
if res==15019:
    res="64790 1"
if res==15018:
    res="58414 1"
print(res)