n, time = int(input()), int(1 / (int(input()) / int(input()))) + 1
aList, pig = [i for i in range(2, time + 2)], 0
for pig in range(1, n):
    if aList[-1] < n:
        aList = [((j + 1) * aList[j - 1] + aList[j] if j > 0 else pig + 2) for j in range(time)]
        continue
    break
print(pig)