num = int(input())

x = input()
xlist = x.split(" ")
array = [int(xlist[i]) for i in range(len(xlist))]

length = 1
maxLength = length
for i in range(num - 1):
    if array[i] < array[i+1]:
        length += 1
    else:
        if maxLength < length:
            maxLength = length
        length = 1
    if i == num - 2:
        if maxLength < length:
            maxLength = length

print(maxLength)
