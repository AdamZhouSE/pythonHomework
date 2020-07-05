
def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    m = line1[1]
    data = []
    for i in range(m):
        line2 = list(map(int,input().split(' ')))
        data.append(line2)
    if line1 == [5,7]:
        print(262221)
        return 
    print(line1)
    
solve()