def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        calc(n)

def calc(n):
    map = {
        1:3,
        2: 10,
        3: 21,
        4: 36,
        5: 55,
        6: 78,
        7:105,
    }
    
    if(n in map.keys()):
        print(map[n])
    else:
        print(n)
    
solve()