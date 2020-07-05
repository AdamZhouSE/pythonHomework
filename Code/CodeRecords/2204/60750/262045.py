
def out(num,res):
    if num == 1:
        res = '1' + ' '
    else:
        if len(res) != 0:
            res = res + str(num) + ' '
        else:
            res = out(num - 1,res)  + str(num) + ' '
    return res




def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        n= int(input())
        tmp = ''
        res.append(out(n,tmp))
    for i in range(test):
        print(res[i])

solve()