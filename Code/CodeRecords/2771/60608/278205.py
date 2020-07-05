
def func20():
    for _ in range(0, eval(input())):
        n: int = eval(input())
        if n <= 0:
            print(0)
        else:
            flag = False
            for i in range(1, n + 1):
                if i * i == n:
                    flag = True
                    break
            if flag:
                print(1)
            else:
                print(0)


func20()
