import sys


def solve():
    src = sys.stdin.readlines()
    map(lambda x:x.strip('\n'),src)
    src.sort()
    print('\n'.join(src))


if __name__ == '__main__':
    solve()