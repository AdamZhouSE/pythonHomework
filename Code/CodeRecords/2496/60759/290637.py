string = input()
ans = []
repeat = []
for ch in set(string):
    repeat.append([ch, string.count(ch)])
repeat.sort(key=lambda x: x[1], reverse=True)
if 2 * repeat[0][1] <= len(string) + 1:
    ans.append(repeat[0][0])
    repeat[0][1] -= 1
    pre = repeat[0][0]
    while len(repeat) > 1:
        repeat.sort(key=lambda x: x[1], reverse=True)
        if repeat[0][0] != pre:
            ans.append(repeat[0][0])
            pre = repeat[0][0]
            repeat[0][1] -= 1
            if repeat[0][1] == 0:
                repeat.pop(0)
        else:
            ans.append(repeat[1][0])
            pre = repeat[1][0]
            repeat[1][1] -= 1
            if repeat[1][1] == 0:
                repeat.pop(1)
    ans.append(repeat[0][0])
print(''.join(ans))
