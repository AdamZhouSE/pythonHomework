n, m = map(int, input().split(" "))

xlist = input().split()
chestNum = [int(xlist[i]) for i in range(n)]
xlist = input().split()
keyNum = [int(xlist[i]) for i in range(m)]

oddKey = []
evenKey = []
oddChest = []
evenChest = []

for chest in chestNum:
    if chest % 2 == 1:
        oddChest.append(chest)
    else:
        evenChest.append(chest)

for key in keyNum:
    if key % 2 == 1:
        oddKey.append(key)
    else:
        evenKey.append(key)

print(min(len(oddKey), len(evenChest)) + min(len(evenKey), len(oddChest)))

