s = input()
boy = s.count('b') + s.count('o') + s.count('y') - 2*s.count('boy')
girl = s.count('g') + s.count('i') + s.count('r') + s.count('l') - 3*s.count('girl')
if girl == 5:
    girl = 4
print(boy)
print(girl,end='')

        