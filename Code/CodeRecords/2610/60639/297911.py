def solution(arr,n):
    count=0
    for i in range(n):
        for j in range(n-i):
            subarr=arr[i:i+j+1]
            if len(set(subarr))==len(subarr):
                count+=len(subarr)
    return count
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split(' ')))
    print(solution(arr,n))