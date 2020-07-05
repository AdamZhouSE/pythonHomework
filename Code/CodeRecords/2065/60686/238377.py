s = input()
list_s = list(s)
invalid_flag = False
flag = False
flag_negative = False
result = 0
for i in range(len(list_s)):
    if not flag:
        if not ('0' <= list_s[i] <= '9' or list_s[i] == ' ' or list_s[i] == '-'):
            invalid_flag = True
            break
        elif list_s[i] == ' ':
            continue
        elif list_s[i] == '-':
            flag_negative = True
            continue
        elif '0' <= list_s[i] <= '9':
            result += int(list_s[i])
            flag = True
    else:
        if not '0' <= list_s[i] <= '9':
            break
        else:
            result *= 10
            result += int(list_s[i])
if flag_negative:
    result = -result
if invalid_flag:
    print(0)
elif result > 2147483647:
    print(2147483647)
elif result < -2147483648:
    print(-2147483648)
else:
    print(result)
