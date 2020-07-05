def num():
    title = input()
    count = 0
    for i in range(0,len(title)):
        if title[i] != ' ' and ord(title[i]) != 10:
            count += 1
    print(count,end = '')

num()