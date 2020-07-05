"""
桌面上水平放置着 n 张卡片，每张卡片在 xi 位置上，不同卡片可能在同一位置上，现规定：
把卡片往左或右移动两个单位不需要费用
往左或右移动一个单位则需要花费一个硬币
现在要将所有卡片都移动到同一个位置上（可以是任意位置），求最少的硬币消耗
"""

n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

odd=0
even=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1

print(min(odd,even))