def func3():
    t = int(input())
    def compute_square_num(n:int)->int:
        res = 0
        while n>0:
            temp = n%10
            n //= 10
            res += temp*temp
        return res
    def is_happy(n:int)->bool:
        quick = compute_square_num(n)
        quick = compute_square_num(quick)
        slow = n
        while quick != 1 and quick != slow:
            quick = compute_square_num(quick)
            quick = compute_square_num(quick)
            slow = compute_square_num(slow)
        return quick == 1
    while t>0:
        t -= 1
        n = int(input())
        while True:
            n += 1
            if is_happy(n):
                print(n)
                break
    return
func3()