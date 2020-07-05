def func11():
    n = int(input())
    s = input().strip()
    y = s.count("0")
    x = s.count("1")
    if x == 0:
        print(0,end="")
    else:
        print(1,end="")
        print("0"*y,end="")
    return
func11()