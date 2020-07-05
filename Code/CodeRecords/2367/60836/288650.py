"""
给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小正整数 N
返回 N 的长度。如果不存在这样的 N，就返回 -1
"""

k=int(input())

div=1
while div<100000:
    if div%k==0:
        break
    else:
        div=div*10+1

if div%k==0:
    print(len(str(div)))
else:
    print(-1)