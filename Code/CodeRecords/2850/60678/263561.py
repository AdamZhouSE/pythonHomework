def countOne(string):
    count = 0
    for i in string:
        if i == '1':
            count += 1
    return count


def turn(start, end, string):
    string = list(string)
    for i in range(start, end + 1):
        if string[i] == '1':
            string[i] = '0'
        else:
            string[i] = '1'
    return string


n = int(input())
nums = input().replace(' ', '')
max = countOne(nums)

for start in range(0, n - 1):
    for end in range(1, n):
        numsCMP = turn(start, end, nums)
        count = countOne(numsCMP)
        if count > max:
            max = count
print(max)