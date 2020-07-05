def isPossible(angles):
    for i in range(2**len(angles)):
        temp = 0
        binStr = getBinary(i)
        while(len(binStr)<len(angles)):
            binStr = "0"+binStr
        for i in range(len(angles)):
            if(binStr[i]=="0"):
                temp += angles[i]
            else:
                temp -= angles[i]
        if(temp%360==0):
            return "YES"
    return "NO"

def getBinary(num):
    return '{:b}'.format(num)


rotateTimes = int(input())
angles = []
for i in range(rotateTimes):
    angles.append(int(input()))
print(isPossible(angles))
