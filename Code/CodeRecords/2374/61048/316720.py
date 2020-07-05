def arr41():
    n=int(input())
    for i in range(n):
        k=int(input())
        arr=[int(x) for x in input().split(' ')]
        hash={}
        for num in arr:
            if(num in hash):
                hash[num]+=1
            else:
                hash[num]=1
        a=sorted(hash.items(), key=lambda x: x[0])

        hash_t = {}
        for k in a:
            hash_t[int(str(k)[1:-1].split(',')[0])]=int(str(k)[1:-1].split(',')[1])

        '''print(hash_t)'''
        a = sorted(hash.items(), key=lambda x: x[1],reverse=True)
        tmp=[]
        for k in a:
            tmp.append([int(str(k)[1:-1].split(',')[0]),int(str(k)[1:-1].split(',')[1])])
        for i in range(len(tmp)-1):
            if(tmp[i][1]==tmp[i+1][1] and tmp[i][0]>tmp[i+1][0]):
                tmp[i],tmp[i+1]=tmp[i+1],tmp[i]

        hash_r = {}
        for k in tmp:
            hash_r[k[0]] = k[1]


        res=""
        for key in hash_r.keys():
            for i in range(hash_r[key]):
                res+=(str(key)+" ")
        print(res)
    return

arr41()