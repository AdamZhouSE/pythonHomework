# https://segmentfault.com/q/1010000009924890

import sys
import re

def solve():
    s=input()
    text=sys.stdin.readlines()
    txt=''.join(text)

    reg=re.compile(s,re.IGNORECASE)
    res=reg.sub('',txt)
    res=res.replace(' ','')
    print(res)

if __name__ == '__main__':
    solve()