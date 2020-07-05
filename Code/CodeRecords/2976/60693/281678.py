tar=input().lower()
len1=len(tar)
x=1
while x<20:
    try:
        str=input()
        tmp=str.lower()
    except EOFError:
        x+=1
        continue
    len2=len(str)
    k,i=0,0
    while i<len2:
        if tmp[i+k]==tar[k]:
            k+=1
            if k==len1:
                i+=k
                k=0
        else:
            if str[i]!=' ':
                print(str[i],end='')
            i+=1
            k=0
    print()