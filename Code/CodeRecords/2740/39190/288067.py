def func5(list):
    list.sort()
    list.append(list[0])
    res=1440
    for i in range(len(list)-1):
        fh,fm=list[i].split(":")
        lh,lm=list[i+1].split(":")
        tmp=int(lh)*60-int(fh)*60+int(lm)-int(fm)
        if tmp>720:
            tmp=1440-tmp
        elif tmp<0:
            tmp=1440+tmp
        res=min(res,tmp)
    print(res)

ip=eval(input())
func5(ip)
