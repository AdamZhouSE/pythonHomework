def func15():
    n = int(input())
    def is_perfect_square(num:int)->bool:
        if num==1:
            return True
        left, right = 0, num
        while left <= right:
            mid = (left+right)//2
            if num == mid*mid:
                return True
            elif num > mid*mid:
                left = mid+1
            else:
                right = mid-1
        return False
    print(is_perfect_square(n))
    return
func15()