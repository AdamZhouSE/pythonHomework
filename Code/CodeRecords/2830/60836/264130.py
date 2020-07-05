"""
有一个整数 n 用以 b 为底的 k 位数表示：
n = a[1]*b^(k-1) + a[2]*b^(k-2) + ... + a[k-1]*b + a[k]
例如, 如果 b=17，k=3，a=[11, 15, 7]，则 n=11*17^2+15*17+7
请判断 n 是奇数还是偶数
"""

bk=[int(m) for m in str(input()).split(" ")]
b=bk[0]
k=bk[1]
a=[int(m) for m in str(input()).split(" ")]

result=0
for i in a:
    result=result+i*(b**(k-1))
    k-=1

if result%2==0:
    print("even")
else:
    print("odd")