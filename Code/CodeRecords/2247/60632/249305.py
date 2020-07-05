data = list(map(int, input().split(',')))
alex, lee = 0, 0
left, right = 0, -1
for i in range(len(data)):
    if i % 2 == 0:
        alex += max(data[left], data[right])
    else:
        lee += max(data[left], data[right])
    if data[left] > data[right]:
        left += 1
    elif data[left] <= data[right]:
        right -= 1
print(alex > lee)
