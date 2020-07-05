str1 = input()
c = 0
for i in range(len(str1)):
    if str1[i].__eq__('('):
        c = c +1
    elif str1[i].__eq__(')'):
        c = c - 1
if c == 0:
    print("YES",end='')
else:
    print("NO",end='')