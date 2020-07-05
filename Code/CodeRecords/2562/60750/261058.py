

def email():
    test = int(input())
    f_unread = []
    f_read = []
    f_trash = []
    for i in range(0,test):
        line1 = list(map(int,input().split(' ')))
        n = line1[0]
        q = line1[1]
        unread = [i+ 1 for i in range(n)]
        read = []
        trash = []
        line2 = list(map(int, input().split(' ')))

        j = 0
        while j < 2* q - 1:
            if line2[j] == 1:
                del unread[unread.index(line2[j+1])]
                read.append(line2[j+ 1])
                j += 2
                continue
            if line2[j] == 2:
                del read[read.index(line2[j + 1])]
                trash.append(line2[j + 1])
                j += 2
                continue
            if line2[j] == 3:
                del unread[unread.index(line2[j + 1])]
                trash.append(line2[j + 1])
                j += 2
                continue
            if line2[j] == 4:
                del trash[trash.index(line2[j + 1])]
                read.append(line2[j + 1])
                j += 2
                continue
        f_unread.append(unread)
        f_read.append(read)
        f_trash.append(trash)

    for i in range(0,test):
        if len(f_unread[i]) == 0:
            print('EMPTY')
        else:
            for j in range(0, len(f_unread[i])):
                print(f_unread[i][j], end=' ')
            print()

        if len(f_read[i]) == 0:
            print('EMPTY')
        else:
            for j in range(0,len(f_read[i])):
                print(f_read[i][j],end = ' ')
            print()

        if len(f_trash[i]) == 0:
            print('EMPTY')
        else:
            for j in range(0, len(f_trash[i])):
                print(f_trash[i][j], end=' ')
            print()

email()
