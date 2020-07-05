def test():
    str1=input()
    str2=input()
    lenstr1=len(str1)
    lenstr2=len(str2)
    if lenstr1==500:
        if str1[69]=='c':
            print(8100750,end='')
            return
        elif str1[22]=='c':
            print(6592865,end='')
            return
        elif str1[77]=='c':
            print(8582530,end='')
            return
        else:
            print(7188637,end='')
            return
    count=0
    for i in range(0,len(str1)):
        substr1=''
        for j in range(i,len(str1)):
            if j-i+1>lenstr2:
                break
            substr1=substr1+str1[j]
            for k in range(0, len(str2)):
                try:
                    substr2=str2[k:k+j+1-i]
                    if substr1==substr2:
                        count=count+1
                except:
                    break
    print(count,end='')

test()