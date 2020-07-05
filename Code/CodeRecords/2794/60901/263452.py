storey = int(input())
books = list(map(int, input().split()))
seek = int(input())
nums = list(map(int, input().split()))
result = []
for num in nums:
    haveSought = 0
    for i in range(storey):
        if haveSought < num and haveSought + books[i] >= num:
            result.append(i+1)
        haveSought += books[i]
for i in result:
    print(i)