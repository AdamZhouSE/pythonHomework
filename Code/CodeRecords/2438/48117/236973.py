randomList = list(input())
randomList.sort()
answer = []
for num in randomList:
    if num >= '0' and num <= '9':
        answer.append(int(num))

print(answer)