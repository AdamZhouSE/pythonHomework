def solve():
    num = int(input())
    str = ''
    for i in range(0,num):
        str = str + chr(i + 65) + str
    print(str)

solve()