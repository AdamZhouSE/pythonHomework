strin = input()
k = input()
x = input()
intarr = []
result = []
for i in range(0,len(strin)):
    if strin[i]!='[' and strin[i]!=']' and strin[i]!=',':
        intarr.append(int(strin[i]))
try:
    temp = intarr.index(int(x))
    if int(k)%2==0:
        if temp<int(k)//2:
            for n in range(0,int(k)):
                result.append(intarr[n])
        elif len(intarr)-temp-1<int(k)//2-1:
            for q in range(len(intarr)-int(k),len(intarr)):
                result.append(intarr[q])
        else:
            for y in range(temp-int(k)//2,temp-int(k)//2+int(k)):
                result.append(intarr[y])
    else:
        if len(intarr)-temp-1<(int(k)-1)//2:
            for j in range(len(intarr)-int(k),len(intarr)):
                result.append(intarr[j])
        elif temp<(int(k)-1)//2:
            for m in range(0,int(k)):
                result.append(intarr[m])
        else:
            for p in range(temp-(int(k)-1)//2,temp-(int(k)-1)//2+int(k)):
                result.append(intarr[p])
    print(result)
except ValueError:
    for o in range(0,int(k)):
        result.append(intarr[o])
    print(result)