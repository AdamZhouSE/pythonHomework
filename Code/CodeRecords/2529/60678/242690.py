import  math

number = list(input())
number.sort()
number = ''.join(number)


nums = []
exp = 0
while 2 ** exp < 10 ** 9:
    nums.append(list(str(2 ** exp)))
    nums[exp].sort()
    nums[exp] = ''.join(nums[exp])
    exp += 1

flagUp = False
for i in nums:
    if i == number:
        flagUp = True
        print('true')
        break
if not flagUp:
    print('false')
