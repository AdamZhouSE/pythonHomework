level = int(input())
capacity = input().split(' ')
book = int(input())
bookNo = input().split(' ')

capacity = [int(x) for x in capacity]
bookNo = [int(x) for x in bookNo]

for e in bookNo:
    i = 0
    while e > capacity[i]:
        e -= capacity[i]
        i += 1
    print(i+1)