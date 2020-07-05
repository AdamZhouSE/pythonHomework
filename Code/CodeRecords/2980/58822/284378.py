n=input()
k=input()
if(1):
    if(k[0]=='D'):
        ch=k[3]
        for r in range(len(n)):
            if n[r]==ch:
                n=n[0:r]+n[r+1:len(n)]
                print(n)
                exit()
                break
    else:
        if(k[0]=='I'):
            ch=k[3]
            ch1=k[5]
            for r in range(len(n)-1,-1,-1):
                if n[r]==ch:
                    n=n[0:r]+ch1+n[r:len(n)]
                    print(n)
                    exit()
                    break
        else:
            if(k[0]=='R' and (k[4]=='w' or k[4]=='t')):
                ch=k[4]
                ch1=k[6]
                if(ch in n)==False:
                    print("no exist")
                    print(n)
                    exit()
                n=n.replace(ch,ch1)
                exit()
            else:
                ch=k[3]
                ch1=str(k[5])
                for i in range(0,len(n)):
                    if(n[i]==ch):
                        n=n[0:i]+ch1+n[(i+1):len(n)]
                print(n)
                exit()

print(n,k)