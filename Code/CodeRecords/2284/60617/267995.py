def biggestSub():
    T=int(input())
    for i in range(0, T):
        n=int(input())
        arr=list(map(int, input().split(" ")))
        findiSubj(n, arr)

def findiSubj(n, arr):
    maxSub=0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i]<=arr[j]:
                maxSub=max(maxSub, j-i)
    print(maxSub)
    
if __name__=='__main__':
    biggestSub()