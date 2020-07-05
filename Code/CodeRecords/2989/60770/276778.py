import sys


def solve():
    src = sys.stdin.readlines()
    src.sort()
    print(''.join(src))


if __name__ == '__main__':
    solve()