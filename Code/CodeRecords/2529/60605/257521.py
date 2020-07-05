# 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
#
# 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

n = input().strip()
length = len(n)
n = sorted(n)
isOK = False
divv = (length-1) // 3
div = (length-1) % 3
begin = divv * 10
end = begin
if div == 0:
    end = begin + 4
elif div == 1:
    begin = begin + 4
    end = begin + 3
else:
    begin = begin + 7
    end = begin + 3
# print(begin, end)
for i in range(begin, end):
    t = pow(2, i)
    if n == sorted(str(t)):
        isOK = True
        break
print(str(isOK).lower())
