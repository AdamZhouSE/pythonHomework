num = int(input())
for i in range(num):
    ppp = input()
    a = input().split(" ")
    list.sort(a)
    z = 0
    count = [1]
    people = [a[0]]
    for j in range(1, len(a)):
        if a[j] == people[z]:
            count[z] = count[z] + 1
        else:
            z = z + 1
            people.append(a[j])
            count.append(1)
    y = list.index(count, max(count))
    print(people[y], max(count))