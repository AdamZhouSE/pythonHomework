p1 = 0
p2 = 0
p3 = 0
a = ''
def deal(x:str,y:str):
    if ord(x) == (ord(y)-1):
        return
    temp = [0]*500
    p = 0
    for i in range(ord(x)+1,ord(y)):
        for j in range(p2):
            if p1 == 1:
                p = p + 1
                temp[p] = chr(i)
            elif p1 == 2 and i>=ord('a') and i<=ord('z'):
                p = p + 1
                temp[p] = chr(i - ord('a')+ord('A'))
            elif p1==2 and i>=ord('1') and i<=ord('9'):
                p = p + 1
                temp[p] = chr(i)
            elif p1 == 3:
                p = p + 1
                temp[p] = '*'

    if p3!=2:
        for i in range(1,p+1):
            print(temp[i],end='')
    else:
        for i in range(p,0,-1):
            print(temp[i],end='')


if __name__ == '__main__':
    line = input().split('  ')
    #print(line)
    p1 = int(line[0])
    p2 = int(line[1])
    p3 = int(line[2])
    a = input()
    len = len(a)
    for i in range(len):
        if a[i] == '-':
            x = a[i-1]
            y = a[i+1]
            if x>='a' and x<='z' and y>='a' and y<='z' or x>='0' and x<='9' and y>='0' and y<='9':
                deal(x,y)
            else:print(a[i],end='')
        else:print(a[i],end='')
    print()