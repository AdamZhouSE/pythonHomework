def do():
    base2=list(input())
    base2=list(map(int,base2))
    base3=list(input())
    base3=list(map(int,base3))
    n2=0
    n3=0
    for i in range(len(base2)):
        n2=0
        base2[i]=1 if base2[i]==0 else 0
        for j in range(len(base2)):
            n2+=base2[j]*(2**(len(base2)-1-j))
        base2[i] = 1 if base2[i] == 0 else 0
        for j in range(len(base3)):
            if base3[j]==0:
                n3=0
                base3[j]=1
                for k in range(len(base3)):
                    n3+=base3[k]*(3**(len(base3)-1-k))
                if n2==n3:
                    return n2
                base3[j]=2
                n3=0
                for k in range(len(base3)):
                    n3+=base3[k]*(3**(len(base3)-1-k))
                if n2==n3:
                    return n2
                base3[j]=0
            elif base3[j]==1:
                n3 = 0
                base3[j] = 0
                for k in range(len(base3)):
                    n3 += base3[k] * (3 ** (len(base3) - 1 - k))
                if n2 == n3:
                    return n2
                base3[j] = 2
                n3 = 0
                for k in range(len(base3)):
                    n3 += base3[k] * (3 ** (len(base3) - 1 - k))
                if n2 == n3:
                    return n2
                base3[j]=1
            elif base3[j]==2:
                n3 = 0
                base3[j] = 0
                for k in range(len(base3)):
                    n3 += base3[k] * (3 ** (len(base3) - 1 - k))
                if n2 == n3:
                    return n2
                base3[j] = 1
                n3 = 0
                for k in range(len(base3)):
                    n3 += base3[k] * (3 ** (len(base3) - 1 - k))
                if n2 == n3:
                    return n2
                base3[j]=2


print(do(),end='')