import math

def check(begin,end):
    div=begin+int((end-begin)/2)
    sum=0
    for i in range(0,len(arr)):
        sum+=math.ceil(arr[i]/div)
    if begin!=end:
        if sum==threshold:
            return div
        elif sum>threshold:
            return check(div+1,end)
        elif sum<threshold:
            return min(div,check(begin,div-1))
    else:
        if sum<=threshold:
            return div
        elif sum>threshold:
            return 1000000


if __name__ == '__main__':
    arr=list(map(int,input().split(",")))
    threshold=eval(input())
    print(check(1,max(arr)))