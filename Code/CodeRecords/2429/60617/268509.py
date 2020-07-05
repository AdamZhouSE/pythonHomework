def maxSub():
    T=int(input())
    for i in range(0, T):
        find_maxSub()

def find_maxSub():
    N=int(input())
    arr=list(map(int, input().split(" ")))
    maxSub=0
    for i in range(0, N-1):
        for j in range(j, N):
            if arr[i]<arr[j]:
                maxSub=max(maxSub, arr[j]-arr[i])
    print(maxSub)
    
if __name__=='__main__':
    maxSub()