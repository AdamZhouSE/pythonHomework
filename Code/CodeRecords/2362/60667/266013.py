N = int(input())
if N <= 4:
    print([1, 2, 6, 7][N-1])
    quit()
mod = N & 3
print(N + [1, 2, 2, -1][mod])
