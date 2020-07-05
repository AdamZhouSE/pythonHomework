n=int(input())
for i in range(n):
    word=list(input())

    num=0
    i=0
    numOfa = 0
    while 'a' in word[i:]:
        if word[i]=='a':
            numOfa+=1
            j=i+1
            numOfb=0
            while 'b' in word[j:]:
                if word[j]=='b':
                    numOfb+=1
                    k = j + 1
                    numOfc = 0
                    while 'c' in word[k:]:
                        if word[k]=='c':
                            numOfc+=1
                            num+=(2**(numOfa-1))*(2**(numOfb-1))*(2**(numOfc-1))
                        k+=1
                j+=1
        i+=1
    print(num)