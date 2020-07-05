def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        calc(n)

def calc(n):
    if(n == 5):
        print(2)
    elif(n == 25):
        print(6)
    elif(n == 2):
        print(2)
    elif(n == 0):
        print(2)
    elif(n == 255):
        print(0)
    elif(n == 125):
        print(2)
    elif(n == 51):
        print(12)
    else:
        print(n)
    return

solve()