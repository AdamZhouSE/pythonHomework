def judge(l):
    for i in l:
        try:
            if i.isdigit() == False:
                raise NameError
        except NameError:
            print("数字类型错误，请输入纯数字!")
            return 0
    else:

        l.sort(reverse=True)
        print(''.join(l), end="")  # 拼接字符串
        return 1


if __name__ == '__main__':

    while True:
        n = int(input())
        l = []
        str = input()
        l = str.split(' ')
        if (judge(l)):
            break
