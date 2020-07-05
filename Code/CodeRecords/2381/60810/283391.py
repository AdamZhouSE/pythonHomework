'''
给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。
数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3。
数组形式 的数字也同样不含前导零：以 arr 为例，这意味着要么 arr == [0]，要么 arr[0] == 1。
返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。
'''

inp1 = input()
arr1 = inp1.split(",")
inp2 = input()
arr2 = inp2.split(",")

len1 = len(arr1)
len2 = len(arr2)
res = []
carry = 0
for i in range(-1, -max(len1, len2) -1, -1):
    v1, v2 = 0, 0
    if(i >= -len1):
        v1 = int(arr1[i])
    if(i >= -len2):
        v2 = int(arr2[i])
    v = v1 + v2 -carry
    carry = v >> 1
    res.append(v & 1)
if (carry == -1):
    res.append(1)
if (carry == 1):
    res.extend([1,1])
while(res[-1] == 0 and len(res) > 1):
    res.pop()
print(res[::-1])
