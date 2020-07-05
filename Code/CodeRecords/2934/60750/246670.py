def solve(password):
    parts = []
    count_left = 0
    count_right = 0
    index = 0
    res = ''

    for i in range(0,len(password)):
        if password[i] == '[':
            count_left += 1
        elif password[i] == ']':
            count_right += 1
        if count_left > count_right:
            continue
        elif count_left == count_right and count_right != 0:
            tmp = password[index:i + 1]
            parts.append(tmp)
            index = i + 1
            count_left = 0
            count_right = 0
        if i == len(password) - 1 and password[i] != ']':
            parts.append(password[index:])

    for i in range(0, len(parts)):
        start = ''
        if (parts[i][0] == '[' and 49 <= ord(parts[i][1]) <= 57):
            for j in range(1, len(parts[i])):
                if 48 <= ord(parts[i][j]) <= 57:
                    start += parts[i][j]
                else:
                    break
            res += solve(parts[i][len(start) + 1:len(parts[i]) - 1]) * int(start)
        elif 49 <= ord(parts[i][0]) <= 57:
            for j in range(0, len(parts[i])):
                if 48 <= ord(parts[i][j]) <= 57:
                    start += parts[i][j]
                else:
                    break
            res += solve(parts[i][len(start):]) * int(start)
        else:
            if parts[i][0]== '[' :
                tmp = ''
                for j in range(1, len(parts[i])):
                    if 65 <= ord(parts[i][j])<= 90:
                        tmp += parts[i][j]
                        res += parts[i][j]
                    else:
                        res += solve(parts[i][len(tmp) + 1:len(parts[i]) - 1])
                        break
            else:
                tmp = ''
                for j in range(0, len(parts[i])):
                    if 65 <= ord(parts[i][j]) <= 90:
                        tmp += parts[i][j]
                        res += parts[i][j]
                    else:
                        res += solve(parts[i][len(tmp) + 1:len(parts[i]) - 1])
                        break
    return res

password = input()
print(solve(password),end = '')


