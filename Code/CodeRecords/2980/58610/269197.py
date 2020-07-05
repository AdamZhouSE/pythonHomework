s = list(input())
command = list(input().replace(' ', ''))
if command[0] == 'D':
    s.remove(command[1])
elif command[0] == 'I':
    index = -s[::-1].index(command[1]) - 1
    s.insert(index, command[2])
elif command[0] == 'R':
    t = [command[2] if x == command[1] else x for x in s]
    if t == s:
        print('no exist')
    s = t
print(''.join(s))