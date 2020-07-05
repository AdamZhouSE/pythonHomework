def func8(list):
    isSame=False
    maxNum=0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            for m in range(len(list[i])):
                for n in range(len(list[j])):
                    if list[i][m]!=list[j][n]:
                        continue
                    else:
                        isSame=True
                        break
                if isSame:
                    isSame=False
                    break
                else:
                    if m==len(list[i])-1 and n==len(list[j])-1:
                        maxNum=max(maxNum,len(list[i])*len(list[j]))
                    else:
                        continue
    return maxNum

ip=eval(input())
res=func8(ip)
print(res)

                    