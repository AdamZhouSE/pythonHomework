input()
stones = list(input())
result = 0
for i in range(0, len(stones)-1):
    if stones[i] == stones[i+1]:
        result += 1
print(result)
