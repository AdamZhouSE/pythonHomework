n = int(input())
nums = list(map(int, input().split(' ')))
books = int(input())
ids = list(map(int, input().split(' ')))
total = []  # total[i]表示前i层放的图书总数
for i in range(n):
    total.append(sum(nums[:i+1]))
for i in ids:
    for j in range(len(total)):
        if i <= total[j]:
            print(j+1)
            break
