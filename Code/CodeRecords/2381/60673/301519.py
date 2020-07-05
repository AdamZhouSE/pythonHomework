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