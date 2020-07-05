def find_n():
    num = int(input())
    if num < 10:
        return num
    string = ''
    for i in range(1, num+1):
        string += str(i)
    return string[num - 1]


print(find_n())