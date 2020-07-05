nums = [x for x in input().split(',')]
times = []
for i1 in range(4):
    for i2 in range(4):
        if i2 == i1:
            continue
        for i3 in range(4):
            if i3 == i2 or i3 == i1:
                continue
            for i4 in range(4):
                if i4 == i1 or i4 == i2 or i4 == i3:
                    continue
                temp = nums[i1] + nums[i2] +':'+ nums[i3] + nums[i4]
                if temp not in times and int(temp[0:2]) < 24 and int(temp[3:5]) < 60:
                    times.append(temp)
times.sort(reverse=True)
if len(times)==0:
    print('')
else:
    print(times[0])
