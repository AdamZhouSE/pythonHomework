def play(list):
    a = [[0] * 101 for i in range(101)]
    x=50
    y=50#shufangxiang
    k=1
    for i in range(0,len(list)):
        if(k==1):
            y=y-list[i]
            if(a[y][x]):
                return True
            else:
                a[y][x]=1
                k+=1
        elif(k==2):
            x=x-list[i]
            if (a[y][x]):
                return True
            else:
                a[y][x] = 1
                k += 1
        elif(k==3):
            y=y+list[i]
            if (a[y][x]):
                return True
            else:
                a[y][x] = 1
                k += 1
        elif (k == 4):
            x = x + list[i]
            if (a[y][x]):
                return True
            else:
                a[y][x] = 1
                k =1
    return False
if __name__ == '__main__':
    list=eval(input())
    print(play(list))