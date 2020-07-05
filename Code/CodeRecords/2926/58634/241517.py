n = int(input())
array1 = [int(i) for i in input().split(" ")]
maxDuplicate = 0
for i in array1:
    maxDuplicate = max(maxDuplicate,array1.count(i))
print (maxDuplicate)
