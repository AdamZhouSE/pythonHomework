def ans(Lohia, Gosu, Prince):
    temp = Prince
    res = []
    cnt = 0
    while(Prince>1):
        if(Lohia%Prince==0):
           cnt += 1
           Lohia -= 1
        else:
            Prince -= 1
    res.append(cnt)
    cnt = 0
    Prince = temp
    while (Prince > 1):
        if (Gosu % Prince == 0):
            cnt += 1
            Gosu -= 1
        else:
            Prince -= 1
    res.append(cnt)
    return res

numOfTests = int(input())
for t in range(numOfTests):
    temp = input().split()
    Lohia = int(temp[0])
    Gosu = int(temp[1])
    Prince = int(temp[2])
    res = ans(Lohia, Gosu, Prince)
    print(res[0],"",end="")
    print(res[1])