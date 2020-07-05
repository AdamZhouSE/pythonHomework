All = int(input())

for q in range(0, All):
    n=int(input())

    ar=n*[0]

    index=0

    out=1
    while out<=n:
        count=0
        while count<out:
            if ar[index]==0:
                count+=1
            index+=1
            index=index%n

        while ar[index]!=0:
            index+=1
            index%=n
        ar[index]=out
        out+=1

    ans=''
    for x in ar:
        ans+=str(x)+' '
    print(ans.strip())

