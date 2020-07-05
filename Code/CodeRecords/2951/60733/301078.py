def convert(n, x):  # n为待转换的十进制数，x为进制，取值为2-16
    list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']  # 注意这里从0开始
    list_b = []
    while True:
        s, y = divmod(n, x)  # divmod()函数返回一个包含商和余数的元组
        list_b.append(y)  # 这里是保存余数
        if s == 0:
            break
        n = s
    list_b.reverse()
    res = ""
    for i in list_b:
        res = res + str(list_a[i])
    return res


def compare(s1, s2):
    if len(s1) != len(s2):
        return 0
    cnt = 0
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            cnt = cnt + 1
    return cnt


def replace_char(string, char, index):
    string = list(string)
    string[index] = char
    return ''.join(string)


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    num = 0
    for i in range(len(s1)):
        if s1[i] == '0':
            s1 = replace_char(s1, "1", i)
        else:
            s1 = replace_char(s1, "0", i)
        num = int(s1, 2)
        rad3 = convert(num, 3)
        if compare(rad3, s2) == 1:
            break
        else:
            if s1[i] == '0':
                s1 = replace_char(s1, "1", i)
            else:
                s1 = replace_char(s1, "0", i)
    print(num,end="")
