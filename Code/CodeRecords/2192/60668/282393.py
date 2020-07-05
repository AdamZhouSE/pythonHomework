def linerlist_4_pr(n):
    co = []
    re = n
    co.append(re)
    if re > 0:
        re -= 5
        co.append(re)
    else:
        re += 5
        co.append(re)
    while re > 0:
        re -= 5
        co.append(re)
    li = len(co)-2
    while li>=0:
        co.append(co[li])
        li-=1
    for i in range(len(co) - 1):
        print(co[i], end=' ')
    print(co[len(co) - 1],end=' \n')


if __name__ == '__main__':
    for _ in range(int(input())):
        n = input()
        linerlist_4_pr(int(n))
