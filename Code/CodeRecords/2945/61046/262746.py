newstr = input()
boy = 0
girl = 0
for i in range(len(newstr)-2):
    if int(ord(newstr[i:i+1])) == int(ord('b')) or int(ord(newstr[i+1:i+2])) == int(ord('o')) or int(ord(newstr[i+2:i+3])) == int(ord('y')):
        boy = boy + 1
for i in range(len(newstr) - 3):
    if int(ord(newstr[i:i+1])) == int(ord('g')) or int(ord(newstr[i+1:i+2])) == int(ord('i')) or int(ord(newstr[i+2:i+3])) == int(ord('r')) or int(ord(newstr[i+3:i+4])) == int(ord('l')):
        girl = girl +1
print(boy)
print(girl,end='')