def tb6():
    n=int(input())
    for i in range(n):
        line1=input().split(' ')
        N,L,R=int(line1[0]),int(line1[1]),int(line1[2])
        tmp=[x for x in str(bin(N))[2:]]
        for j in range(len(tmp)-R,len(tmp)-L+1):
            tmp[j]='0' if tmp[j]=='1' else '1'
        res=""
        for x in tmp:
            res+=x
        res="0b"+res
        print(int(res,2))
    return

tb6()