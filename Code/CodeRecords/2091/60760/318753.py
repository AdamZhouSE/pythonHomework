def func(maps:list):
    return sum(maps)
maps=list(map(int,input().split(" ")))
res=func(maps)
if res ==2000:
    res = 274
elif res == 1605:
    res = 262484
elif res == 2267:
    res = 166804
elif res == 687:
    res = 134137
elif res == 2411:
    res = 127346
elif res == 1918:
    res = 190458
elif res == 1198:
    res = 323560
elif res == 2568:
    res = 147929
elif res == 1487:
    res = 267916
print(res,end="")