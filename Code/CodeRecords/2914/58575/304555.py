n=int(input())
for i in range(n):
    number=int(input())
    a=list(map(int,input().split(" ")))
    b=list(map(int,input().split(" ")))

    i=0
    while i<number:
        if a[i]!=b[i]:
            break
        i+=1
    if i==number:
        print("YES")
    else:
        k=a[i]-b[i]
        if k>0:
            print("NO")
        else:
            j=i
            while j<number:
                if a[j]==b[j]:
                    break
                else:
                    b[j]=b[j]+k
                j+=1
            if a==b:
                print("YES")
            else:
                print("NO")