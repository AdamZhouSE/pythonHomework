def single():
    ls = eval(input())
    num = ls[0]
    for i in range(1, len(ls)):
        num = num ^ ls[i]
    return num


print(single())