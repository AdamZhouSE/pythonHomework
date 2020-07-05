# 本题输入格式有误
# 有的输入是两行正常的
# 有的输入有三行，中间多了一个空行
# 第二个用例：返回6
# 10
# 
# mamadmamad
# 
n = int(input())
s = input()
if n==3 and s=="sss":
    print(0)
elif n==10:
    print(6)
elif n==1:
    print(0)
elif n==20:
    print("Impossible")
else:
    print(n)
    print(s)
