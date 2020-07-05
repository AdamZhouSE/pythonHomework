def func6():
    a = input()
    screen = ""  #记录凹槽中的字符串
    prints = []  #记录打印出的字符串
    for i in range(len(a)):
        if a[i] == "P":
            prints.append(screen)
        elif a[i] == "B":
            screen = screen[:-1]
        else:
            screen += a[i]
    def helper(x: str, y: str)->int:
        res = 0
        while len(y) >= len(x):
            if y.find(x) != -1:
                res += 1
                y = y[y.find(x)+1:]
            else:
                break
        return res
    n = int(input())
    while n > 0:
        n -= 1
        temp = list(map(int, input().split(" ")))
        if temp[0] > len(prints) or temp[1] > len(prints):
            print(0)
        else:
            print(helper(prints[temp[0]-1], prints[temp[1]-1]))
    return
func6()