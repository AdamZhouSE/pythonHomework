nums_of_tests = int(input())
res = []
for i in range(nums_of_tests):
    num = int(input())
    arrival = input().split(" ")
    leave = input().split(" ")
    arrival = [int(i) for i in arrival]
    leave = [int(i) for i in leave]
    trains = []
    for j in range(num):
        trains.append([arrival[j], leave[j]])
    count = 0
    groups = [0]
    for p in range(len(trains) - 1):
        q = p + 1
        if groups.count(p) == 0 or p == 0:
            while q < len(trains):
                if trains[p][1] <= trains[q][0]:
                    p = q
                    groups.append(p)
                    q = p + 1
                q += 1
            count += 1
    res.append(count)
for i in res:
    print(i)