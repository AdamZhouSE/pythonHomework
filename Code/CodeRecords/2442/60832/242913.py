ar=list(map(int,(input().lstrip('[').rstrip(']')).split(",")))
if len(ar)<2:
    print(0)
else:
    ar.sort()
    Max=ar[1]-ar[0]
    for i in range(1,len(ar)-1):
        if ar[i+1]-ar[i]>Max:
            Max=ar[i+1]-ar[i]
    print(Max)