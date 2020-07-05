import math
"""
给出数字 N，返回由若干 "0" 和 "1"组成的字符串，该字符串为 N 的负二进制（base -2）表示
除非字符串就是 "0"，否则返回的字符串中不能含有前导零
"""

N=int(input())

re=[]
while N!=1:
    if N%(-2)==(-1):
        re.append(1)
    else:
        re.append(0)
    N=math.ceil(N/(-2))

re.append(1)
re.reverse()
print("".join(map(str,re)))
