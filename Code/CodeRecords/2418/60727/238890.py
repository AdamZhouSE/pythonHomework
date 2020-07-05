tomato = int(input())
cheese = int(input())
if tomato==0 and cheese == 0:
    print('[0, 0]')
if tomato/cheese==4.0:
    print('['+tomato//4+', 0]')
if tomato/cheese==2.0:
    print('['+tomato//4+', ]')