def password():
    num = int(input())
    article = input()
    res = ''
    for i in range(0,len(article)):
        if ord(article[i]) + num <= 122:
            res += chr(ord(article[i]) + num)
        else:
            tmp = ord(article[i]) + num
            while tmp > 122:
                tmp = tmp - 26
            res += chr(tmp)
    print(res,end = '')

password()