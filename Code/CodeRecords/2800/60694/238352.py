x = input()
xlist = x.split(" ")
n = int(xlist[0])
d = int(xlist[1])

x = input()
xlist = x.split(" ")
array = [int(xlist[i]) for i in range(len(xlist))]

count = 0
for i in range(len(array) - 1):
    while array[i] >= array[i+1]:
        array[i+1] += d
        count += 1

print(count)
