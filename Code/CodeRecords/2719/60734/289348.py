n = int(input())
meetings = []
for i in range(n):
    line = input()
    if line == 'B':
        print(len(meetings))
    else:
        op, l, r = line.split(' ')
        l, r = int(l), int(r)
        cnt = 0
        i = 0
        while i < len(meetings):
            if meetings[i][0] <= l <= meetings[i][1] or meetings[i][0] <= r <= meetings[i][1]:
                meetings.pop(i)
                cnt += 1
                i -= 1
            i+=1
        meetings.append([l,r])
        print(cnt)