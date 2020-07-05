def compare(x,y):
    if x[0] == y[0] or x[1] == y[1]:
        return 1
    else:
        return 0


nums = int(input())
al = []
for i in range(nums):
    points = int(input())
    total = 0
    list = []
    for j in range(points):
        list.append(input().split(" "))
        for k in range(j):
            total += compare(list[j], list[k])
            if list[j]==['0','1'] and list[i]==['1','1']:
                total-=1
    al.append(total)
for i in al:
    print(i)