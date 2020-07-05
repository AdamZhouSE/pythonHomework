n=int(input())
a=list(map(int,input().split(" ")))
if n==1:
    print("YES")
else:
    i=1
    while i<n and a[i]>a[i-1]:
        i=i+1
    if i==n:
        print("NO")
    else:
        while i<n and a[i]==a[i-1]:
            i=i+1
        if i==n:
            print("YES")
        else:
            flag="YES"
            while i<n:
                if a[i]>=a[i-1]:
                    flag="NO"
                    break
                i=i+1
            print(flag)