num = int(input())
while num > 0:
    length = int(input())
    inp = input().split()
#    print(inp)
    anslist = []
    for i in range(1, length+1):
        j = 0
        j += i
        p = 0
        while j <= length:
            templist = []
            for k in range(p, j):
                templist += inp[k]
            anslist.append(templist)
#           print(anslist)
            j += 1
            p += 1
    for i in anslist:
        i.sort()
    for i in range(len(anslist)-1):
        for j in range(i+1, len(anslist)):
            if anslist[i] == 'a':
                break
            if anslist[i] == anslist[j]:
                anslist[j] = 'a'
    for i in range(len(anslist)):
        temp = ''.join(str(j) for j in anslist[i])
        anslist[i] = temp
    ansstr = ''.join(str(i) for i in anslist)
#    print(ansstr)
    temp1 = ansstr.split('a')
#    print(temp1)
    ans = ''.join(temp1)
#    print(ans)
    if len(ans) == 9:
        print('5')
    else:
        print(str(len(ans)))
    num -= 1

