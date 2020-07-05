def solve(k):
    n = k + 1
    table = [0 for i in range(k+2)]
    for i in range(1,k+2):
        if i % 2 == 1:
            table[i] = k-int(i/2)+1
        else:
            table[i] = int(i/2)
    ans = ' '.join(list(map(str,table[::-1][:-1]))) + ' '
    print(n)
    print(ans,end='')

k = int(input())
solve(k)