def check():
    begin=0
    end=1
    while True:
        mid=(begin+end)/2

        sum=0
        p=0
        q=-1
        for i in range(0,len(arr)):
            temp=0
            for j in range(len(arr)-1,-1,-1):
                up=arr[i]
                down=arr[j]
                if up/down<=mid:
                    temp+=1
                    if up/down>p/q:
                        p=up
                        q=down
                else:
                    sum+=temp
                    break
        if sum==k:
            return [p,q]
        elif sum<k:
            begin=mid
        else:
            end=mid


if __name__ == '__main__':
    arr=eval(input())
    k=eval(input())
    print(check())