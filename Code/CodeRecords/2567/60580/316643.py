def input_manage():
    temp = input()
    temp = temp[1:len(temp) - 1]
    temp = temp.split(',')
    return temp


def judge(array, window_length, upper, lower):
    count = 0
    for i in range(len(array) - window_length + 1):
        num = add(array, i, i + window_length)
        if lower <= num and num <= upper:
            count = count + 1
    return count


def add(array, start, end):
    num = 0
    for i in range(start, end):
        num = num + int(array[i])
    return num


array = input_manage()
lower = int(input())
upper = int(input())
window_length = len(array)
count = 0
while window_length > 0:
    count = count + judge(array, window_length, upper, lower)
    window_length = window_length - 1
print(count)
