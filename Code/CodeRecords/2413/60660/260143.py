#Leestcode1238 格雷码+数组截断
'''什么是格雷码
在一组数的编码中，若任意两个相邻的代码只有一位二进制数不同，则称这种编码为格雷码（Gray Code）,
另外由于最大数与最小数之间也仅一位数不同，即“首尾相连”，因此又称循环码或反射码。

如何求解格雷码
生成格雷码的方法: n+1位格雷码G(n+1)总数 等于 n位格雷码G(n)总数的2倍。
只需将n位格雷码G(n)最高位添加0作为G(n+1)的前一半数据(符合格雷码要求)即不变
然后G(n)逆序排,并在最高位加1,作为G(n+1)的后一半数据(也符合格雷码要求),即G(n)每一位加上1<<(n)。
'''
n=int(input())
start=int(input())
grey=[0,1]
if (n==1):
    print(start,1-start)
else:
    for i in range(1,n):
        for j in range(len(grey)-1,-1,-1):
            grey.append(grey[j]+(1<<i))
            if grey[j]+(1<<i) == start:
                id=len(grey)-1
result=grey[id:]
result+=grey[0:id]
print(result)
