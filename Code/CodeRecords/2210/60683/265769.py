T = eval(input())
for i in range(T):
    candidate = input()
    target = input().strip()
    temp = list(target)
    left = 0
    right = 0
    sz = len(candidate)
    ans = ''
    res = [0, sz + 1]
    while True:
        while right < sz:
            if candidate[right] in temp:
                temp.remove(candidate[right])
                if len(temp) == 0:
                    break
            right += 1
        if right == sz:
            break
        # res = [left, right]
        while candidate[left] not in target or candidate[left] in candidate[left+1:right]:
            left += 1
        temp.append(candidate[left])
        if right - left < res[1] - res[0]:
            res = [left, right]
        left += 1
    if res[1]==sz+1:
        print(-1)
        print()
    else:
        print(candidate[res[0]:res[1]+1])
# print()