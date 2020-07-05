num = int(input())

x = input()
xlist = x.split(" ")
aSet = set(xlist)

if aSet.__contains__("0"):
    aSet.remove("0")

print(len(aSet))




