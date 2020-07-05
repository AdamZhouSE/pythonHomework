def solve():
    str = input()
    str = str[1:len(str)-1]
    str = ''.join(str.split(','))

    print(int(str, 2))



solve()