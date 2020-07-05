arr=input()
list=[int(n) for n in arr.split(',')]
le=len(list)
for i in range(0,le+1):
    mark=0
    for j in range(0,le):
        if list[j]==i:
            mark=1
    if mark==0:
       print(i)
       break