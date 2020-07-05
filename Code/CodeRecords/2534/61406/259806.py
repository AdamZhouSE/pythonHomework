source = input().replace('[', '').replace(']', '')
list1 = source.split(',')
list1.sort()
print([int(x) for x in list1])