str = input()
res = ""
cou = 0
for i in range(0,len(str)-1):
    for j in range(i+1,len(str)+1):
        tem = str[i:j]
        has = 0
        for h in range(i+2,len(str)):
            if str[h]==tem[0] and len(str)-h>=j-i:
                tmp = str[h:h+j-i]
                if str[h:h+j-i]==tem:
                    if cou<j-i:
                        res = tem
                        cou = j-i
                        has = 1
        if has == 0:
            break

print(res)