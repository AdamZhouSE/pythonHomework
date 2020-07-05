num = input().split(",")
numbers = [int(i) for i in num]
target = int(input())
ind = len(numbers) - 1
while numbers[ind] >= target:
    ind -= 1
result = []
haveFind = False
for i in range(ind):
    for j in range(i+1, ind+1):
        if numbers[i] != numbers[j] and numbers[i] + numbers[j] == target:
            result.append(i+1)
            result.append(j+1)
            haveFind = True
            break
    if haveFind:
        break
if haveFind:
    print(result)
else:
    print("None")
