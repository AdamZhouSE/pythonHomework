"""
现在给定 n 个整数，请使用其中任意个整数（每个只能使用一次），得到一个最大的为偶数的和
"""

n=int(input())
arr=[int(k) for k in str(input()).split(" ")]

odd=[]
ad=0
for i in arr:
    if i%2==0:
        ad=ad+i
    else:
        odd.append(i)

if len(odd)%2==0:
    ad=ad+sum(odd)
else:
    ad=ad+sum(odd)-min(odd)

print(ad)
