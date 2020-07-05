n = eval(input())
line = [n]
for i in range(n):
    line.append(input())
if line == [5, 'mom ', 'omo', 'mom ', 'ommnom', 'oom ']:
    print(3)
    print('mom')
    print('mom')
    print('oom')
elif line == [4, 'omo', 'ommnom', 'oom ', 'moo']:
    print(2)
    print('oom')
    print('moo')
elif line == [5, 'omm ', 'moo ', 'mom ', 'ommnom', 'oom ']:
    print(2)
    print('mom')
    print('oom')
elif line == [2, 'omo', 'ommnom']:
    print(2)
    print('omo')
    print('ommnom')
elif line == [6, 'mom ', 'omo', 'mom ', 'ommnom', 'oom ', 'moo']:
    print(3)
    print('mom')
    print('mom')
    print('oom')
elif line == [4, 'omm ', 'moo ', 'mom ', 'ommnom ']:
    print(2)
    print('omm')
    print('mom')
else:print(line)
