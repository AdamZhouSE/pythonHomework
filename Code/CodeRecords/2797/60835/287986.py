n = int(input())
group = list(map(int,input().split()))
res= ""
if group[-1] == 15:
    res = "DOWN"
elif group[-1] == 0:
    res = "UP"
elif len(group) > 1:
    if group[-1] - group[-2] > 0:
        res = "UP"
    elif group[-1] - group[-2] < 0:
        res = "DOWN"
    else:
        res = "-1"
else:
    res = "-1"
print(res)