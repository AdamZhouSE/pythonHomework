s=input()
t=input()
arrS=[]
arrT=[]
for i in range(len(s)):
    arrS.append(s[i])
for i in range(len(t)):
    arrT.append(t[i])
beginning=0
judge=1
for i in range(len(arrS)):
    currentArea=arrT[beginning:len(arrT)]
    if arrS[i] in currentArea:
        beginning=arrT.index(arrS[i])
    else:
        judge=0
        break
print(judge==1)