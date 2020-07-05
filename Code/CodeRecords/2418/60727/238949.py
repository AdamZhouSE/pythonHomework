tomato = int(input())
cheese = int(input())
if tomato==0 and cheese == 0:
    print('[0, 0]')
if tomato==4*cheese:
    print('[{}, 0]'.format(tomato//4))
if tomato==2*cheese:
    print('[0, {}]'.format(tomato//2))