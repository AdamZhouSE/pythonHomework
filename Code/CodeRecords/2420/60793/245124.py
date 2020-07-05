
def no_zero(num):
    ls = list(str(num))
    for x in ls:
        if x == '0':
            return False
    return True


the_num = int(input())
for i in range(1, int(the_num / 2) + 1):
    if no_zero(i) and no_zero(the_num - i):
        print([i, the_num - i])
        break
