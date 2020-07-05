def func44():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        nums = list(map(int, input().split(" ")))
        odd, even = [], []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        even.sort()
        odd.sort(reverse=True)
        for i in odd:
            print(i,end=" ")
        for i in even:
            print(i,end=" ")
        print()
    return
func44()