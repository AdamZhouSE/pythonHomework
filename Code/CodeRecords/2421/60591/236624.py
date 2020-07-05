n = input()
temp = list(n)
for x in range(len(temp)):
    if(temp[x] == '6'):
        temp[x] = '9'
        break
print(''.join(temp))