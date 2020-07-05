def baseNeg2(N):
    if N == 0:
        return '0'
    res = ''
    while N != 0:
        tmp = N % (-2)
        if tmp == 0:
            res = '0' + res
        else:
            res = '1' + res
        N = (N + tmp) / (-2)
    return res
def cal(numbers):
    result = 0
    temp = numbers.copy()
    temp.reverse()
    basic = 1
    for number in temp:
        result += number * basic
        basic *= -2
    return result

string1 = input()
string2 = input()
nums1 = list(map(int,string1.split(",")))
nums2 = list(map(int,string2.split(",")))
num1 = cal(nums1)
num2 = cal(nums2)
num = num1 + num2
result = list(map(int,baseNeg2(num)))
print(result)