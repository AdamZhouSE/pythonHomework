n = int(input())
ping1 = [0,0]
ping2 = [0,0]
for i in range(0,n):
    s = input().split(' ')
    if(s[0] == '1'):
        ping1[0] = ping1[0] + int(s[1])
        ping1[1] = ping1[1] + int(s[2])
    else:
        ping2[0] = ping2[0] + int(s[1])
        ping2[1] = ping2[1] + int(s[2])
if(ping1[0] >= ping1[1]):
    print('LIVE')
else:
    print('DEAD')
if(ping2[0] >= ping2[1]):
    print('LIVE')
else:
    print('DEAD')