numbers = [int(n) for n in input().split(',')]
target = int(input())
left, right = 0, len(numbers) - 1
while left<right:
    tmp = numbers[left] + numbers[right]
    if tmp == target:
        print( [left + 1, right + 1])
        break
    elif tmp < target:
        left += 1
    elif tmp > target:
        right -= 1
if left == right:
    print('None')