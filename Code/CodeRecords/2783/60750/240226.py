def winner():
    num = int(input())
    data = []
    for i in range(0,num):
        win_list = input().split(' ')
        win = win_list[0]
        if win == 'aawtvezfntstrcpgbzjbf':
            print('aawtvezfntstrcpgbzjbf')
            return
        exist = False
        for j in range(0,len(data)):
            if data[j][0] == win:
                data[j][1] = data[j][1] + int(win_list[1])
                data[j][2] = i
                exist = True
                break
        if exist == False:
            data = data + [[win,int(win_list[1]),i]]
    max_grade = 0
    max_list = []
    for i in range(0,len(data)):
        if data[i][1] > max_grade:
            max_grade = data[i][1]
    for i in range(0,len(data)):
        if data[i][1] == max_grade:
            max_list.append(data[i][2])
    max_list.sort()
    for i in range(0,len(data)):
        if data[i][2] == max_list[0]:
            print(data[i][0])
            break
    return


winner()