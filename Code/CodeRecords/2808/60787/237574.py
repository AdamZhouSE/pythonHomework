n=int(input())
list=[int(i) for i in input().split()]
max=list.index(max(list))
min=list.index(min(list))
if max>min:
    if n-1-max>min:
        print(n-1-min)
    else:
        print(max)
else:
    if n-1-min>max:
        print(n-1-max)
    else:
        print(min)