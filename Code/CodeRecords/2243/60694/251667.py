p = int(input())
q = int(input())

while p % 2 == 0 and q % 2 == 0:  # 退出循环后p, q至少有1个为奇数
    p /= 2
    q /= 2

'''
规律（水平/竖直方向增加虚房间总结归纳得出）：
p为奇数，q为奇数时，到达接收器1。
p为奇数，q为偶数时，到达接收器0。
p为偶数，q为奇数时，到达接收器2。
'''

if p % 2 == 1 and q % 2 == 1:
    print(1)
elif p % 2 == 1 and q % 2 == 0:
    print(0)
elif p % 2 == 0 and q % 2 == 1:
    print(2)
