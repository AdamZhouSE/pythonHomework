info = input().split()
length = int(info[0])
nums = int(info[1])
str_ope = input()
ask = []
for i in range(nums):
    info = input().split()
    a = int(info[0])
    b = int(info[1])
    c = int(info[2])
    d = int(info[3])
    ask.append([a, b, c, d])
for i in range(nums):
    a = ask[i][0]
    b = ask[i][1]
    c = ask[i][2]
    d = ask[i][3]
    len_list = []
    for j in range(a - 1, b):
        for k in range(j + 1, b + 1):
            sub = str_ope[j:k]
            sec = str_ope[c - 1:d]
            cnt = 0
            for p in range(len(sub)):
                if p <= len(sec) - 1:
                    if sub[p] == sec[p]:
                        cnt = cnt + 1
                    else:
                        break
                else:
                    break
            len_list.append(cnt)
    maxLen = max(len_list)
    print(maxLen)