def function(l, start, time):
    sum = 0
    count = 0
    for i in range(start, len(l)):
        sum += l[i]
        count += 1
        if sum > time:
            count -= 1
        else:
            continue
    return count


s1 = input().split(' ')
s2 = input().split(' ')
l1 = []
l2 = []
for i in range(len(s1)):
    l1.append(int(s1[i]))
for i in range(len(s2)):
    l2.append(int(s2[i]))

result = []
for i in range(len(l2)):
    result.append(function(l2, i, l1[1]))

print(max(result))