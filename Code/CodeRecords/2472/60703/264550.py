T = int(input())
res= []
for m in range(T):
    n =int(input())
    strr = list(input())
    sett = set(strr)
    for i in range(len(strr)):
        temp = strr[i]
        if temp not in strr[:i]+strr[i+1:]:
            res.append(temp)
            break
        else:
            if i==len(strr)-1:
                res.append("-1")


for i in res:
    print(i)