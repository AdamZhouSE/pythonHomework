array = [int(i) for i in input().split(",")]
d = int(input())
maxL = 1
for i in range(len(array)):
    length = 1
    previous = array[i]
    for j in range(i, len(array)):
        if array[j] == previous + d:
            length += 1
            previous = array[j]
    maxL = max(length,maxL)
print(maxL)
