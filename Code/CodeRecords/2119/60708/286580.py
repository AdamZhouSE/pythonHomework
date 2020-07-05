def play(list):
    a = [[0] * 11 for i in range(11)]
    x=5
    y=5#shufangxiang
    a[5][5]=1
    k=1
    for i in range(0,len(list)):
        if(k==1):
            k += 1
            newy=y-list[i]
            while(y!=newy):
                y-=1
                if(not a[y][x]):
                    a[y][x]=1
                else:
                    return True
        elif(k==2):
            k += 1
            newx=x-list[i]
            while (x != newx):
                x -= 1
                if (not a[y][x]):
                    a[y][x] = 1
                else:
                    return True
        elif(k==3):
            k += 1
            newy = y + list[i]
            while (y != newy):
                y += 1
                if (not a[y][x]):
                    a[y][x] = 1
                else:
                    return True
        elif (k == 4):
            k=1
            newx = x + list[i]
            while (x != newx):
                x += 1
                if (not a[y][x]):
                    a[y][x] = 1
                else:
                    return True
    return False
if __name__ == '__main__':
    list=eval(input())
    print(play(list))