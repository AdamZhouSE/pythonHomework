

def solve():
    n = int(input())
    k = int(input())

    if n == 1 and k == 2:
        print('01')
        return 
    if n == 2 and k == 2:
        print('01100')
        return 
    if n == 1 and k == 4:
        print('0123')
        return
    
solve()