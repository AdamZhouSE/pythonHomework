def minNum():
    n = int(input())
    str1 = input()
    count = 0
    res = ''
    for i in range(0,n):
        if str1[i] == '1':
            count += 1

    if count != 0:
        res = '1'
    for i in range(0,n - count):
        res = res + '0'
    print(res,end = '')

minNum()