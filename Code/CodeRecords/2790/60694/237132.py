x = input()
xlist = x.split(" ")

lenA = int(xlist[0])
lenB = int(xlist[1])

x = input()
xlist = x.split(" ")
elementsA = [int(xlist[i]) for i in range(len(xlist))]

x = input()
xlist = x.split(" ")
elementsB = [int(xlist[i]) for i in range(len(xlist))]

count = 0
times = 0 # 记录外层循环次数
for b in elementsB:
    times += 1
    for a in elementsA:
        if a <= b:
            count += 1
    print(count, end="")
    if times != len(elementsB):
        print(" ", end="")
    count = 0
print()