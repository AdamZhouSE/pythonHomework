# 第n个丑数肯定是由前n-1个数中的某个数乘上a，b，c
import heapq
def cal(n,a,b,c):
    q = [1]
    for i in range(1,n): #弹出n-1个不同的，顶上的一个就是需要的元素
        val = heapq.heappop(q)
        while q and q[0] == val: #去掉重复的
            heapq.heappop(q)
        for i in [a,b,c]:
            heapq.heappush(q,i*val)
    return q[0]
    


n = int(input())
a = int(input())
b = int(input())
c = int(input())
print(cal(n,a,b,c))