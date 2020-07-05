while(True): 
    n = int(input())
    if(n == 0):
        break
    modeLst = []
    for i in range(0,n):
        mode = input()
        modeLst.append(mode)
    s = input()
    rec = [0,'']
    for m in modeLst:
        count = 0
        for i in range(0,len(s) - len(m) + 1):
            temp = s[i: i + len(m)]
            if(temp == m):
                count = count + 1
        if(count > rec[0]):
            rec = [count,m]
        elif(count == rec[0]):
            rec.append(m)
    for r in rec:
        print(r)
