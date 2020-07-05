num = input()
strin = input()
intarr = []
for i in range(0,len(strin)):
    if strin[i]!=' ':
        intarr.append(int(strin[i]))
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
for j in range(0,len(intarr)):
    if intarr[j]==1:
        cnt1 = cnt1 + 1
    elif intarr[j]==2:
        cnt2 = cnt2 + 1
    elif intarr[j]==3:
        cnt3 = cnt3 + 1 
    else:
        cnt4 = cnt4 + 1
result = cnt4
if cnt3>=cnt1:
    result = result + cnt3
    if cnt2%2==0:
        result = result + cnt2/2
    else:
        result = result + cnt2//2 + 1
else:
    result = result + cnt3
    cnt1 = cnt1 - cnt3
    if cnt2%2==0:
        result = result + cnt2/2
        if cnt1%4==0:
            result = result + cnt1/4
        else:
            result = result + cnt1//4 + 1
    else:
        result = result + cnt2//2
        if cnt1<=2:
            result = result + 1
        else:
            result = result + 1
            cnt1 = cnt1 - 2
            if cnt1%4==0:
                result = result + cnt1/4
            else:
                result = result + cnt1//4 + 1
print(int(result))
