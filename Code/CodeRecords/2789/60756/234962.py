firstLine=input()
k=int(firstLine)
for i in range(k):
    n=int(input())
    nLen=input().split()
    nLen.sort(key=int)
    for j in range(1,n+1):
        if j>=int(nLen[n-j]):
            print(max(int(nLen[n-j]),j-1))
            break
        if j==n:
            print(n)