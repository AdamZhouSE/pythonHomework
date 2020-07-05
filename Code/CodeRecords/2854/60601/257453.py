def solve(num:list):
    num.sort()
    fourNo = -1
    for i in num:
        if num.count(i)==6:
            return 'Elephant'
        if num.count(i)>=4:
            fourNo = i
            break
    if fourNo!=-1:
        num.remove(fourNo)
        num.remove(fourNo)
        num.remove(fourNo)
        num.remove(fourNo)
        if num[0] == num[1]:
            return 'Elephant'
        else:
            return 'Bear'
    else:
        if num != [1, 2, 3, 7, 8, 9] and num !=[1, 2, 3, 4, 5, 6] and num !=[1, 1, 1, 2, 3, 5]:
            print(num)
        return 'Alien'
    pass
num = list(map(int,input().split(' ')))
print(solve(num))
