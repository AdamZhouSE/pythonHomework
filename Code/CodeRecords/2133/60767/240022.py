inp = input().split(",")
arr = []
for i in inp:
    arr.append(int(i))
minNum = min(arr)
totalNum = sum(arr)
print(totalNum-len(arr)*minNum)