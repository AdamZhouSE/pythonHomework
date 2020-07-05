t=eval(input())
for _ in range(t):
    n =eval(input())
    num = bin(n).replace('0b', '')
    strL = len(num)
    if strL % 2 == 1:
        num = '0' + num
    strL = len(num)
    m = strL // 2
    res=''
    for i in range(m):
        temp1 = num[2 * i]
        temp2 = num[2 * i + 1]
        res=res+temp2+temp1
    result=int(res,2)
    print(result)