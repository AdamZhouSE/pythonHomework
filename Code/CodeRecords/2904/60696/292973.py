if __name__ == '__main__':
    num = input()
    n = len(num)
    temp = []
    sign = 1
    for i in range(n):
        if num[i] == '-':
            sign = -1
            continue
        else:
            temp.append(num[i])
    temp.reverse()
    print(sign * int(''.join(temp)))