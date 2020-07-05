def test():
    t = int(input())
    for _ in range(0, t):
        n=int(input())
        binary=bin(n).replace('0b','')
        one=0
        zero=0
        for i in range(0,len(binary)):
            if binary[i]=='0':
                zero=zero+1
            else:
                one=one+1
        bin_one=bin(one).replace('0b','')
        bin_zero=bin(zero).replace('0b','')
        length=max(len(bin_one),len(bin_zero))
        while len(bin_one)<length:
            bin_one='0'+bin_one
        while len(bin_zero)<length:
            bin_zero='0'+bin_zero
        res=["0"]*length
        for i in range(0,length):
            if bin_one[i]!=bin_zero[i]:
                res[i]='1'
            else:
                res[i]='0'
        res=''.join(res)
        res=int(res,2)
        print(res)

test()