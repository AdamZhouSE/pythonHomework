def test():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        binary = bin(n).replace('0b', '')
        res = [n]
        for i in range(0, n):
            andRes=[]
            binary_i = bin(i).replace('0b', '')
            while len(binary_i)<len(binary):
                binary_i='0'+binary_i
            for j in range(0,len(binary_i)):
                if binary_i[j]=='1' and binary[j]=='1':
                    andRes.append('1')
                else:
                    andRes.append('0')
            andRes=''.join(andRes)
            andRes=int(andRes,2)
            if andRes==i:
                res.append(andRes)
        res.sort(reverse=True)
        result=' '.join(list(map(str,res)))+' '
        print(result)




test()