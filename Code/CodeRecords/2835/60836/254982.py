"""
Jeff 得到了 n 张纸牌，每张纸牌的数字要么是数字 0，要么是数字 5
Jeff 可以选择多张纸牌，并将它们排成一行，以得到某个数
请问，Jeff 可以从纸牌得到的数中，能够被 90 整除的最大数是多少？
Jeff 必须组成不含前导 0 的数。为此，我们还假定数 0 不含任何的前导 0。Jeff 不必使用所有的纸牌
"""

n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

num_of_five=0
num_of_zero=0
for i in arr:
    if i==5:
        num_of_five=num_of_five+1
    if i==0:
        num_of_zero=num_of_zero+1

if num_of_five//9>=1 and num_of_zero>=1:
    print("555555555"*(num_of_five//9)+"0"*num_of_zero)
elif num_of_zero==0:
    print("-1")
else:
    print("0")