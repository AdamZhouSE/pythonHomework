K=int(input())
def CountZero(num):
	res=0
	while num>0:
		num//=5
		res+=num
	return res


large, small = 5 * K + 5, 4 * K  # 首先找到上下界
middle = (large + small) // 2
while CountZero(middle) != K and large - small > 1:  # 此处是为了确保middle能在范围里面
	if CountZero(middle) > K:
		large = middle
	else:
		small = middle
	middle = (large + small) // 2

middle1 = middle
while CountZero(large) != K and large - middle1 > 1:
	temp = (middle1 + large) // 2
	if CountZero(temp) > K:
		large = temp
	else:
		middle1 = temp

while CountZero(large) != K and large >= small: large -= 1
while CountZero(small) != K and small <= large: small += 1
if CountZero(small) != K: print(0)
else:
	print(large-small+1)
