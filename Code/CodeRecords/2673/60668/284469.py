def linelist_28_gery(n):
    n ^= n >> 16
    n ^= n >> 8
    n ^= n >> 4
    n ^= n >> 2
    n ^= n >> 1
    return n
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        print(linelist_28_gery(int(n)))