"""
奥尔加来看望双胞胎安娜和玛丽亚，看到他们有许多饼干，饼干被分到袋子里。
因为有很多饼干，奥尔加决定偷一包。不过，她不希望姐妹俩在分饼干时无缘无故吵架
这就是为什么奥尔加想偷一包饼干，这样剩下的袋子里的饼干数量可以平均地分成两份
请问有多少种偷一袋饼干的方法，这样剩下的袋子里的饼干总数是偶数？
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

num=0
if odd%2==0:
    num=num+even
else:
    num=num+odd
    
print(num)
