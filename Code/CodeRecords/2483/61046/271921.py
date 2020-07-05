num = int(input())
string = []
patt = []
resnum = []
ans = []
for i in range(num):
    # tempStr = input()
    string.append(input())
    # tempPatt = input()
    patt.append(input())

for i in range(num):
    tempPatt = list(patt[i])
    tempStr = list(string[i])
    for j in range(len(tempPatt)):
        # for k in range(len(tempStr)):
        if tempPatt[j] in tempStr:
            resnum.append(tempStr.index(tempPatt[j]))
            ans.append(tempPatt[j])
        else:
            resnum.append(1000)
            ans.append("$")
    if min(resnum) != 1000:
        print(tempStr[min(resnum)])
        ans = []
        resnum = []
    else:
        print('$')
        ans = []
        resnum = []