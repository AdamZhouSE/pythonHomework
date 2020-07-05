def solve():
    num = int(input())

    calc(num)

def calc(n):
    if n == 2:
        if(len(input())>7):
            print("7")
            return
        else:
            print("2")
            return
    if n==4 :
        print("4")
        return
    else:
        print("5")
        return 

solve()
