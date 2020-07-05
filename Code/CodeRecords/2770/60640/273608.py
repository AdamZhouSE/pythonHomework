"""
对会议时间按照结束时间升序排序
每场会议有3个数据，开始时间，结束时间，原来的位置
[start,end,position]
从第二个开始，开始时间大于前一个结束时间，加入到结果中
"""
t = int(input())
for i in range(t):
    n = int(input())
    s = input().strip(" ")
    t = input().strip(" ")
    meet_start = [int(x) for x in s.split(" ")]
    meet_end = [int(x) for x in t.split(" ")]
    # print(meet_start)
    # print(meet_end)
    meet = []
    for j in range(n):
        meet.append([meet_start[j], meet_end[j], j+1])
    # 按照第二项结束时间排序
    meet = sorted(meet, key=lambda x: x[1])
    # 将第一项的位置加入到结果中
    res = [meet[0][2]]
    curr_end_time = meet[0][1]
    for j in range(1, n):
        # 会议开始时间在前一场结束时间之后
        if meet[j][0] > curr_end_time:
            res.append(meet[j][2])
            # 更新会议结束时间
            curr_end_time = meet[j][1]
    for j in range(len(res)):
        print(res[j], end=" ")
    print()