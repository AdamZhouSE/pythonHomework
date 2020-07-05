name = list(input())
st = int(input())

iname = ''
for i in name:
    i = ord(i) - 65 + st
    iname += str(i)


while (int(iname) > 100):
    temp = ''
    for i in range(len(iname) - 1):
        temp += str((int(iname[i]) + int(iname[i+1])) % 10)
    iname = temp
    
print(int(iname),end='')
        
    