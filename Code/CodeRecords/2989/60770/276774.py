import sys

def solve():
    src=sys.stdin.readlines()
    strs=src.split('\n')
    strs.sort()
    print(strs)
    
if  __name__ == '__main__' :
    solve()