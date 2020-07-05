def solve(n):
    res = []
    for i in range(n,-1,-1):
        if n & i == i:
            res.append(i)
    for each in res:
        print(each,end=' ')
    print()
    

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        solve(num)