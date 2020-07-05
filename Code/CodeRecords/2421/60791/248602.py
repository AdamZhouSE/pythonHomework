num = str(input())
l1 = list(num)
for i in range(len(l1)):
    if(l1[i] == '6'):
        l1[i] = '9'
        break
num = ''.join(l1)
print(num)
