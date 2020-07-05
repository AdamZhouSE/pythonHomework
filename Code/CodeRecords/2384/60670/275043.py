n=int(input())
arr=list(map(int,input()))
for i in range(1,n+2):
    if not(i in arr):
        print(i)
        break