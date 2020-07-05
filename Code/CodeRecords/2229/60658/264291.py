li = list(map(int,input().split(',')))
floor = len(li)
for i in range(len(li)-1,1,-1):
    floor = min(floor,li[i])
    if li[i-2]>floor:
        print(False)
        exit()
print(True)
#o(n)
li = list(map(int,input().split(',')))
floor = len(li)
print(all(abs(i-x)<=1 for i,x in enumerate(li)))