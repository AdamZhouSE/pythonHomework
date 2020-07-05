s = input()


def sum(string, result):
    temp_sum = 0
    for i in range(len(string)):
        temp_sum += int(string[i])
    if temp_sum > 10:
        return sum(str(temp_sum), 0)
    else:
        return temp_sum


res = sum(s, 0)
print(res)
