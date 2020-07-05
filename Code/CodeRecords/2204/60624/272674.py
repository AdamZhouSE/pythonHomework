def func10():
    t = int(input())
    def prints(n):
        if n>0:
            prints(n - 1)
            print(n, end=" ")
    while t>0:
        t -= 1
        n = int(input())
        prints(n)
        print()
    return
func10()