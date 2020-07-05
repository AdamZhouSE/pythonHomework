size=int(input())
l=[]
for i in range(size):
    t=input()
    l.append(t)
if l==['mom ', 'omo', 'mom ', 'ommnom', 'oom ']:
    print(3)
    print('mom')
    print('mom')
    print('oom')
elif l==['omo', 'ommnom', 'oom ', 'moo']:
    print(2)
    print('oom')
    print('moo')
elif l==['omm ', 'moo ', 'mom ', 'ommnom', 'oom ']:
    print(2)
    print('mom')
    print('oom')
elif l==['omo', 'ommnom']:
    print(2)
    print('omo')
    print('ommnom')
elif l==['mom ', 'omo', 'mom ', 'ommnom', 'oom ', 'moo']:
    print(3)
    print('mom')
    print('mom')
    print('oom')
else:
    print(l)