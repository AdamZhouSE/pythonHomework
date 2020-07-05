def conflict(time1, time2):
    if time1[1] < time2[0] or time2[1] < time1[0]:
        return False
    return True


timeline = []
n = int(input())
for _ in range(0, n):
    operation = input()
    if operation == "B":
        print(len(timeline))
    else:
        [start, end] = operation[2:].split(" ")
        count = 0
        i = 0
        while i < len(timeline):
            if conflict(timeline[i], [start, end]):
                timeline.pop(i)
                count += 1
                i -= 1
            i += 1
        print(count)
        timeline.append([start, end])
