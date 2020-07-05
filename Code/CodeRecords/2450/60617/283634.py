def firstAndlast():
    arr = input().split(",")
    num = []
    for item in arr:
        num.append(int(item[0]))
    target = int(input())
    left = 0
    right = len(num) - 1
    res=[-1, -1]
    while left <= right:
        mid=(left+right)//2
        if num[mid]==target:
            if num[mid-1]==target:
                res[0]=mid-1
                res[1]=mid
                print(res)
                exit()
            elif num[mid+1]==target:
                res[0]=mid
                res[1]=mid
                print(res)
                exit()
            else:
                res[1]=mid
                res[0]=mid
                print(res)
                exit()
        if target>num[mid]:
            left=mid+1
        else:
            right=mid-1
        print(num)
        print(target)

if __name__=='__main__':
    firstAndlast()