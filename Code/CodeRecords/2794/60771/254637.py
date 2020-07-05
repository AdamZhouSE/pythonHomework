#39
n = int(input())
ori = input().split(" ")
books = [int(item) for item in ori]
m = int(input())
ori = input().split(" ")
nums = [int(item) for item in ori]
outcome = []
for item in nums:
    sum = 0
    for i in range(0,n):
        sum += books[i]
        if item <= sum:
            outcome.append(i+1)
            break
for item in outcome:
    print(item)