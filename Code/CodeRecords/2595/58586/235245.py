lines=int(input())
for i in range(lines):
    arr=list(map(int,input().split(" ")))
    n=arr[0]
    k=arr[1]
    print(pow(k,n-1))
    i+=1