num1 = int(input())  # 说的数字个数

x = input()
xlist = x.split(" ")

num2 = xlist.count("1")  # 楼梯个数
print(num2)

tempList = xlist
indexList = []

for i in range(num2):
    indexList.append(tempList.index("1"))
    tempList[tempList.index("1")] = "/"

indexList.append(num1)

for i in range(len(indexList) - 1):
    print(indexList[i+1] - indexList[i], end="")
    if i != len(indexList) - 2:
        print(" ", end="")
print()