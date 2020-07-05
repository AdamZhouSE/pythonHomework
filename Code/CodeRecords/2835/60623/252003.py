# # 被2整除，个位是偶数，三（九）：各位数之和是三（九）的倍数，四：末两位被四整除，六：各位数之和是三倍数的偶数八：末两位被八整除
# Jeff 得到了 n 张纸牌，每张纸牌的数字要么是数字 0，要么是数字 5。Jeff 可以选择多张纸牌，并将它们排成一行，以得到某个数。
# 请问，Jeff 可以从纸牌得到的数中，能够被 90 整除的最大数是多少？
# Jeff 必须组成不含前导 0 的数。为此，我们还假定数 0 不含任何的前导 0。Jeff 不必使用所有的纸牌。
size=int(input())
strList=input().split()
intList=[]
for var in strList:
	intList.append(int(var))
d={}
for var in intList:
	if var in d.keys():
		d[var]+=1
	else:
		d[var]=1
if d[0]==0:
	print(-1)
else:
	while (5*d[5])%9!=0:
		d[5]=d[5]-1
		if d[5]<=0:
			print(-1)
			break
	if d[5]>0:
		temp=""
		for i in range(d[5]):
			temp+=str(5)
		for i in range(d[0]):
			temp+=str(0)
		print(temp)