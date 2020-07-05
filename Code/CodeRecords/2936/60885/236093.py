def normalize(num):
    nums = list(num.replace('-', ''))
    for i in range(len(nums)):
        if not ('A' <= nums[i] <= 'Z'):
            continue
        c = ord(nums[i])
        if 0 <= ord('C') - c <= 2:
            nums[i] = '2'
        elif 0 <= ord('F') - c <= 2:
            nums[i] = '3'
        elif 0 <= ord('I') - c <= 2:
            nums[i] = '4'
        elif 0 <= ord('L') - c <= 2:
            nums[i] = '5'
        elif 0 <= ord('O') - c <= 2:
            nums[i] = '6'
        elif 0 <= ord('S') - c <= 3:
            nums[i] = '7'
        elif 0 <= ord('V') - c <= 2:
            nums[i] = '8'
        elif 0 <= ord('Y') - c <= 2:
            nums[i] = '9'
    result = ''.join(nums)
    return result[0:3] + '-' + result[3:]

def init():
    numbers = {}
    for i in range(int(input())):
        num = normalize(input())
        if num in numbers:
            numbers[num] += 1
        else:
            numbers[num] = 1
    result = sorted(numbers.items(), key=lambda x:x[0])
    output = []
    for phone, count in result:
        if count >= 2:
            output.append('%s %d'%(phone, count))
    if len(output) == 0:
        print('No duplicates.', end='')
    else:
        for line in output:
            print(line)

init()