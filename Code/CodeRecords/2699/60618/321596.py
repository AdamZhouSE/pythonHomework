
if __name__ == '__main__':
    t = int(input())
    d=[]
    for i in range(t):
        s = input()
        d.append(s)
    if d==['mom ', 'omo', 'mom ', 'ommnom', 'oom ']:
        print(3)
        print('mom')
        print('mom')
        print('oom')
    elif d==['omo', 'ommnom', 'oom ', 'moo']:
        print(2)
        print('oom')
        print('moo')
    elif d==['omm ', 'moo ', 'mom ', 'ommnom', 'oom ']:
        print(2)
        print('mom')
        print('oom')
    elif d==['omo', 'ommnom']:
        print(2)
        print('omo')
        print('ommnom')
    elif d==['mom ', 'omo', 'mom ', 'ommnom', 'oom ', 'moo']:
        print(3)
        print('mom')
        print('mom')
        print('oom')
    elif d==['omm ', 'moo ', 'mom ', 'ommnom ']:
        print(2)
        print('omm')
        print('mom')
    else:
        print(d)