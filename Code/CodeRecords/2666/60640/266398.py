"""
因为一个同学在收到别人发的信息后再发送时，会包含两个人的信息
所以只要n-1个人将信息发个剩下的一个人，再由他发给n-1个人即可
即2*(n-1)
"""
t = int(input())
for i in range(t):
    n = int(input())
    res = 2*(n-1)
    print(res)
