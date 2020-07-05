def isPossible(a,b):#b个数字要不一样哦
    if b>a:
        return 0
    lst1=[i for i in range(1,b+1)]
    min_sum=sum(lst1)
    if a<min_sum:
        return 0
    return 1


if __name__=="__main__":
    tests=int(input())
    cnt=0
    while cnt<tests:
        lst=input().split()
        res=isPossible(int(lst[0]),int(lst[1]))
        print(res)