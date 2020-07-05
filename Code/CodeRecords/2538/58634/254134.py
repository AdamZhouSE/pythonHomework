a = [int(i) for i in input().replace("[","").replace("]","").replace(","," ").split(" ")]
a.sort()
for i in range(0,a[-1]+1):
    if a.count(i+1) == 0 and i+1>0:
        print(i+1)
        break