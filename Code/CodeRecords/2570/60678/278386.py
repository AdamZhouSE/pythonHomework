def canBeInside(listA, listB):
    if listA[0] < listB[0] and listA[1] < listB[1]:
        return True
    return False


n = int(input())
letters =[]
for i in range(0, n):
    letters.append(input().split(","))
    letters[-1][0] = int(letters[-1][0])
    letters[-1][1] = int(letters[-1][1])

letters.sort()
counts = []
for start in range(0, len(letters)):
    count = 1
    index = start + 1
    preW = letters[start][0]
    preH = letters[start][1]
    while index < len(letters):
        if letters[index][0] > preW and letters[index][1] > preH:
            count += 1
            preW = letters[index][0]
            preH = letters[index][1]
        index += 1
    counts.append(count)
counts.sort()
print(counts[-1])