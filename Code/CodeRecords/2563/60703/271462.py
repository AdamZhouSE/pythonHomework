num = int(input()[1:-1])
def solution(num:int):
    import math
    m = int(math.log(num,2))
    for i in range(m,0,-1):
        l = 2
        r = int(pow(num,1/i))+1
        mid = 0
        sum = 0
        while l<r:
            if(l==r):
                sum = 0
                for j in range(i):
                    sum = sum * mid + 1

                if sum == num:
                    return mid

                break
            mid = (l+r)//2
            sum = 1
            for j in range(i):
                sum = sum*mid+1

            if sum==num:
                return mid

            elif(sum<num):
                l = mid+1
            else:
                r = mid
    # return

print(solution(num))