All = int(input())

for q in range(0, All):
    length = int(input())
    ar = list(map(int, input().split()))

    i=0
    while i<length:
        temp=ar[i]
        del ar[i]
        ar.insert(i+1,temp)
        i+=2

    ans=''
    for x in ar:
        ans+=str(x)+' '
    print(ans.strip())