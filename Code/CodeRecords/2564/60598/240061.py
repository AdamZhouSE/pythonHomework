array = list(map(int, input()[1:-1].split(",")))
number = int(input())-1
target = int(input())
Min = array[-1]
for i in range(len(array)):
    if abs(target-array[i]) < Min:
        Min = abs(target-array[i])
        position = i
left = position-1
right = position + 1
result = [array[position]]
count = 0
while left >= 0 and right < len(array):
    if target - array[left] <= array[right]-target:
        result.insert(0,array[left])
        left -= 1
    else:
        result.append(array[right])
        right += 1
    count += 1
    if count == number:
        break
if count == number:
    print(result)
else:
    if left < 0:
        result = result + array[right:right+number-count]
    else:
        result = array[left-(number-count):left]+result
    print(result)
