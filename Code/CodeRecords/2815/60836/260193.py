"""
现在有一组 n 个数 a1, a2, ..., an
每一步你可以选择一个数加上或减去 1
现在想要让 a⋅a2⋅...⋅an=1 即这些数的乘积为 1，请问至少需要多少步？
"""

n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

step=0
num_0=0
num_01=0
for i in arr:
    if i<0:
        step+=-1-i
        num_01+=1
    elif i>0:
        step+=i-1
    else:
        step+=1
        num_0+=1

if num_01%2==1 and num_0==0:
    print(step+2)
else:
    print(step)