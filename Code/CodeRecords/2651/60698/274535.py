def test():
    t = int(input())
    for _ in range(0, t):
        n=int(input())
        str_bin=bin(n)
        str_bin=str_bin[2:]
        if len(str_bin)%2!=0:
            str_bin='0'+str_bin
        list_bin=list(str_bin)
        for i in range(0,len(list_bin)):
            if i%2==0:
                tmp=list_bin[i]
                list_bin[i]=list_bin[i+1]
                list_bin[i+1]=tmp
        res=''.join(list_bin)
        res=int(res,2)
        print(res)




test()