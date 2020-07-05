def stock(n: int, stocks: list) -> str:
    profit = 0
    begin = -1
    res = []
    for i in range(n):
        if begin == -1 and i + 1 != n and stocks[i] < stocks[i+1]:
            begin = i
        if begin != -1 and ((i+1 != n and stocks[i] > stocks[i+1]) or i == n - 1):
            profit += (stocks[i] - stocks[begin])
            res.append((begin, i))
            begin = -1
    if profit == 0:
        return '没有利润'
    else:
        string = ''
        for i in range(len(res)-1):
            string += '(' + str(res[i][0]) + ' ' + str(res[i][1]) + ')' + ' '
        string += '(' + str(res[len(res)-1][0]) + ' ' + str(res[len(res)-1][1]) + ')'
        return string


t = int(input())
ans = []
for j in range(t):
    num = int(input())
    stock_ls = input().split(' ')
    stock_ls = list(map(int, stock_ls))
    ans.append(stock(num, stock_ls))
for k in ans:
    print(k)