n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
q = [int(i) for i in input().split()]
for i in q:
    count = 0
    sum = a[0]
    if i<=sum:
        print(1)
        continue
    while i>sum:
        count += 1
        sum += a[count]
        if i<=sum:
            print(count+1)