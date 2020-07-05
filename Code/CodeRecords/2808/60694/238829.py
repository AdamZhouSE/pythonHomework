num = int(input())

xlist = input().split()
array = [int(xlist[i]) for i in range(num)]

minIndex = array.index(min(array))
maxIndex = array.index(max(array))

if minIndex == 0 or maxIndex == 0:
    print(num-1)
elif minIndex == num-1 or maxIndex == num-1:
    print(num-1)
else:
    print(max(minIndex-0, num-1-minIndex, maxIndex-0, num-1-maxIndex))


