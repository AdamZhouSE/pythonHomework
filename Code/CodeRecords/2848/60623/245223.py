# 给定两个数组 A 和 B，由整数组成，按非递减顺序排序。
# 请检查是否可以在数组 A 中选择 k 个数字，在数组 B 中选择 m 个数字，使得数组 A 中所选数字都严格小于数组 B 中所选数字。
a=input()
select=input().split()
aL=input().split()
bL=input().split()
aL.sort()
bL.sort()
if int(aL[int(select[0])-1])<int(bL[len(bL)-int(select[1])]):
	print("YES")
else:
	print("NO")