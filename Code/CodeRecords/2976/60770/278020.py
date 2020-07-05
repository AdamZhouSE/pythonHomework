import sys


def solve():
    s=input()
    text=sys.stdin.readlines()
    text.repleace(s,'')
    print(text)
    
if __name__ == '__main__':
    solve()