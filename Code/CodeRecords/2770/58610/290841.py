for _ in range(eval(input())):
    meeting_num = eval(input())
    meet = zip(list(map(int, input().strip().split(' '))), list(map(int,input().strip().split(' '))),
                   list(range(1, meeting_num + 1)))
    meet = sorted(meet, key=lambda x: x[0])
    res = []
    for i in range(meeting_num):
        temp_res = []
        for j in range(i):
            if meet[j][1] <= meet[i][0]:
                temp_res = max(temp_res, res[j], key=lambda x: len(x))[:]
        temp_res.append(meet[i][2])
        res.append(temp_res)
    print(*max(res, key=lambda x: len(x)), end=' \n')