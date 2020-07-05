def addOne(s):
    carry = 1
    result = ''
    for c in s[::-1]:
        if c == '0':
            result = str(carry) + result
            carry = 0
        elif c == '1':
            if carry == 1:
                result = '0' + result
            else:
                result = '1' + result
                carry = 0
    if carry == 1:
        result = '1' + result
    return result

def test():
    N = int(input())
    ans = ['1']
    for i in range(N-1):
        ans.append(addOne(ans[-1]))
    return ' '.join(ans) + ' '

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)
