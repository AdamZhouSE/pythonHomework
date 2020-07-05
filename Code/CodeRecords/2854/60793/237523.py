from collections import Counter
sticks = list(map(int, input().split(" ")))
sticksDict = Counter(sticks)
resultLs = sorted(sticksDict.values())
if resultLs == [2, 4]:
    print("Elephant")
elif resultLs == [1, 1, 4]:
    print("Bear")
else:
    print(resultLs)