ntc = list(map(int, input().split()))
level = list(map(int, input().split()))
if ntc[0] < ntc[2]:
    print(0)
else:
    result = 0
    for i in range(0, len(level)):
        bl = True
        if i + ntc[2] <=len(level):
            for j in range(i, i + ntc[2]):
                if level[j]>ntc[1]:
                    bl=False
                    break
            if bl:
                result=result+1
    print(result)
                 
           



