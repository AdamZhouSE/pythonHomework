source=input()  #没看懂题目
length=len(source)
for n in range(1,length+1):
    str0=source[0:n]
    mistery = 0
    l=len(str0)
    for i in range(1,l):
        for j in range(l+1):
            temp=str0[i:j]
            for lens in range(l):
                if i>=1 and j>i and j <= i+lens-1 and i+lens-1<j+lens-1 and j+lens-1<=l and str0[i-1:i+lens-1]==str0[j-1:j+lens-1]:
                    #print(str0,str0[i-1:i+lens-1],i,j)
                    mistery=mistery+lens
    print(mistery)