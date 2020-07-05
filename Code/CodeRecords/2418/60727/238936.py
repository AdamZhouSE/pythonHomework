tomato = int(input())
cheese = int(input())
if tomato==0 and cheese == 0:
    print('[0, 0]')
if tomato//cheese==4:
    print('[{}, 0]'.format(tomato//4))
if tomato//cheese==2:
    print('[0, {}]'.format(tomato//2))