T = int(input())

for k in range(0, T):
    num = int(input())
    temp = list(input().split(" "))
    k = int(input())
    lists = []

    for x in temp:
        lists.append(int(x))

    i = 0
    a=False
    while i < len(lists):
        j = i+1
        while j < len(lists):
            if lists[i] + lists[j] == k:
                print(str(lists[i]) + " " + str(lists[j]) + " " + str(k))
                lists.remove(lists[j])
                j = j - 1
                lists.remove(lists[i])
                i = i - 1
                a=True
            j=j+1
        i=i+1

    if not a:
        print(-1)
