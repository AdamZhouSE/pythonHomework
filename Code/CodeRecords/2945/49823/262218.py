def aa(s):
    a,b,i=0,0,0
    while i<len(s):
        if s[i]=='b':
            a+=1
            i+=3
        elif s[i]=='o':
            a+=1
            i+=2
        elif s[i]=='y':
            a+=1
            i+=1
        else:
            i+=1
    i=0
    while i<len(s):
        if s[i]=='g':
            b+=1
            i+=4
        elif s[i]=='i':
            b+=1
            i+=3
        elif s[i]=='r':
            b+=1
            i+=2
        elif s[i]=='l':
            b+=1
            i+=1
        else:
            i+=1
    print(a)
    print(b,end='')
if __name__ == '__main__':
    aa(input())
