for i in range(int(input())):
    lst=list(map(int,input().split()))
    toBecomputed=int(input())
    answer=lst[0]+(lst[1]-lst[0])*(toBecomputed-1)
    print(answer)