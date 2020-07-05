num = int(input())
for j in range(num):
    n, k = list(map(int, input().split()))
    people = []
    for i in range(1, n + 1):
        people.append(i)
    pos = k - 1
    while len(people) != 1:
        people.pop(pos)
        pos += k-1
        while pos >= len(people):
            pos -= len(people)
    print(people[0])
