from collections import Counter
sticks = list(map(int, input().split(" ")))
sticksDict = Counter(sticks)
resultLs = sorted(sticksDict.values())
if resultLs == [2, 4] or resultLs == [6]:
    print("Elephant")
elif resultLs == [1, 1, 4] or resultLs == [1, 5]:
    print("Bear")
else:
    print("Alien")