"""
第一个数组中最少移动几个元素可以与第二个数组相等
"""
n = int(input())
in_tunnel = [int(x) for x in input().split(" ")]
out_tunnel = [int(x) for x in input().split(" ")]
count = 0
for i in range(n):
    if in_tunnel[i] != out_tunnel[i]:
        count += 1
        # 出现不相等后，移动所需元素到该位置，剩余元素保持顺序
        c = in_tunnel
        c.remove(out_tunnel[i])
        c.insert(0, out_tunnel[i])
        in_tunnel = c
print(count)
