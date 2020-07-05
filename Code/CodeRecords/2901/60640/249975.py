"""
交替位二进制数
如果是01间隔排列，那么右移一位与原数异或得到的二进制数所有位必然全是1
"""
inp = int(input())
tmp = inp ^ (inp >> 1)
if tmp & (tmp+1) == 0:
    print(True)
else:
    print(False)
