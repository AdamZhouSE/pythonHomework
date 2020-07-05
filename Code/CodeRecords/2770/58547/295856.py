def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        input()  # eat
        start = [int(x) for x in input().split()]
        finish = [int(x) for x in input().split()]

        meetings = []
        j = 0
        while j < len(start):
            meetings.append([start[j], finish[j], j])
            j += 1

        meetings.sort(key=lambda x: x[1])
        # sort meetings by finishing time

        res = [meetings[0][2]]  # index of meetings[0]
        j = 1
        while j < len(start):
            if meetings[j][0] >= finish[res[-1]]:
                res.append(meetings[j][2])
            j += 1

        for ele in res:
            print(ele + 1, "", end="")
        print()

        i += 1


func()
