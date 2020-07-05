num = int(input())
string = []
patt = []
resnum = []
#ans = []
for i in range(num):
    string.append(input())
    patt.append(input())

for i in range(num):
    tempPatt = list(patt[i])
    tempStr = list(string[i])
    for j in range(len(tempPatt)):
        if tempPatt[j] in tempStr:
            resnum.append(tempStr.index(tempPatt[j]))
        else:
            resnum.append(1000)
    if min(resnum) != 1000:
        print(tempStr[min(resnum)])
        resnum = []
    else:
        print('$')
        resnum = []