def solution():
    n=int(input())
    arr=list(map(int,input().split()))
    judge=0
    for i in range(1,n-1):
        if arr[i]==max(arr[0:i+1]) and arr[i]==min(arr[i:len(arr)]):
            judge=1
            result=arr[i]
            break
        else:
            continue
    if judge==1:
        print(result)
    else:
        print(-1)

def main():
    T=int(input())
    for i in range(T):
        solution()

main()

