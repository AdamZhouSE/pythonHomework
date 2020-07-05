n = int(input())
boys = list(map(int,input().split()))
n = int(input())
girls = list(map(int,input().split()))
cnt = 0
his1 = sorted(boys)
his2 = sorted(girls)
his3 = []
boys.sort()
girls.sort()
while len(boys) > 0 and len(girls) > 0:
    #print(boys,girls)
    n = 0
    while n < len(girls):
        if girls[n] -1 == boys[0] or girls[n] +1 == boys[0] or girls[n] == boys[0]:
            his3.append([girls[n],boys[0]])
            break
        else:
            n = n + 1
    if n != len(girls):
        cnt = cnt + 1
        del girls[n]
    del boys[0]
'''
if cnt == 4:
    print(his1)
    print(his2)
    print(his3)
    '''
print(cnt)