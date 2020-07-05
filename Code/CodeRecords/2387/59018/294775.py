'''注意： L R是指数组中第几个元素 若n=6则从第一个到第六个 没有第0个 ！！！
         排序是指 把数组中第L个到第R个元素排序 即[L-1,R-1] 即a[L-1：R]！！！
         q也是指第q个元素！！！即为a[q-1]
   
'''

n1, m1 = input().split(' ')      
n = int(n1)
m = int(m1)
info = input().split(' ')
a = [int(y) for y in info]
for i in range(m):
    OP1, L1, R1 = input().split(' ')
    OP = int(OP1)
    L = int(L1)
    R = int(R1)
    c = []
    d = []

    if OP==0:
        a = sorted(a[L - 1:R]) + a[R:]
    else:
        a = sorted(a[L - 1:R],reverse=True) + a[R:]

q = int(input())
print(a[q-1])
    