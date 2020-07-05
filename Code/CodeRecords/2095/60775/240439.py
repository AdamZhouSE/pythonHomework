a = input()
b = input()
carry = 0
if len(a)>len(b):
    len_result = len(a)
    b = '0'*(len_result-len(b)) + b
else:
    len_result = len(b)
    a = a + '0'*(len_result-len(a))

result = []

for i in range(len_result):
    result.append(0)

for i in range(-1,len_result*(-1)-1,-1):
    result[i] = int(a[i]) ^ int(b[i]) ^ carry
    carry = (int(a[i])&int(b[i])) | (int(a[i])&carry) | (int(b[i])&carry)

if carry == 1:
    print(1,end='')
for i in result:
    print(i,end='')
print()