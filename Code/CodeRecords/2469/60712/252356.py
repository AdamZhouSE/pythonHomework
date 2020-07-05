n = int(input())
l = []
for i in range(n):
    temp = list(input())
    temp2 = temp[0:len(temp)]
    temp2.sort()

    #find kinds of different letter
    dif = 1
    for j in range(len(temp2)-1):
        if temp2[j]!=temp2[j+1]:
            dif+=1
    if dif ==1:
        print(1)
    else:

        for j in range(dif,len(temp2)+1):
            isFind=False
            for k in range(len(temp2)):
                d=1
                if j+k <= len(temp2):
                    t = temp[k:j+k]
                    t.sort()
                   # print(t)
                    for m in range(len(t)-1):
                        if t[m]!=t[m+1]:
                            d +=1
                    if d == dif:
                        print(j)
                        isFind =True
                        break
                if isFind:
                    break
            if isFind:
                break







