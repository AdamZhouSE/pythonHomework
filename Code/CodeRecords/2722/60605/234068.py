# 题目描述
# 给定一个整数N，您必须确定它是否是Anshuman的最爱。
#
# 如果是，则打印“YES”，否则打印“NO”。
#
# 如果数字是整数5的和或差，则它是Anshuman的最爱。（5 + 5、5 + 5 + 5、5-5、5-5-5 + 5 + 5…..）
#
# 输入描述
# 输入的第一行包含一个整数，表示测试用例的数量。输入的下一行包含要测试的整数N。
#
# 输出描述
# 对于每个测试用例，根据给定的数字N是否是Anshuman的最爱，输出将在新行中包含答案为“YES”或“NO”。

t = int(input())
li = []
for i in range(t):
    li.append(int(input()))

for i in range(t):
    if li[i] % 5 == 0:
        print("YES")
    else:
        print("NO")