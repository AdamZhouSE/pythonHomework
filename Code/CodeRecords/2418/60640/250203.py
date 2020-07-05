"""
不浪费原料的汉堡制作方案
列方程解决问题
两个已知整数x,y
4a+2b=x
a+b=y
得到：
a = (x-2y)/2
b = (4y-x)/2
注意这里a，b都要大于等于0
"""
tomatoSlices = int(input())
cheeseSlices = int(input())
ans = []
total_jumbo = (tomatoSlices-2*cheeseSlices)//2
total_small = (4*cheeseSlices-tomatoSlices)//2
if (tomatoSlices-2*cheeseSlices) % 2 == 0 and (4*cheeseSlices-tomatoSlices) % 2 == 0 and total_jumbo >= 0 and total_small >= 0:
    ans.append(total_jumbo)
    ans.append(total_small)
    print(ans)
else:
    print(ans)
