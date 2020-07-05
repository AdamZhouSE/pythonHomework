s=input()
dic=list(eval(input()))
dic.sort()
dic.sort(key = lambda i:len(i),reverse=True)
for i in range(len(dic)):
    temp=dic[i]
    rec,success=0,True
    for j in range(len(temp)):
        if s.find(temp[j],rec)!=-1:
            rec=s.index(temp[j])
        else:
            success=False
            break
    if success:
        print(temp)
        exit()
            