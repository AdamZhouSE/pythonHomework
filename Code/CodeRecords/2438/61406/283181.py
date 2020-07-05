source = input().lstrip('[').rstrip(']').split(',')
source.sort()
print([int(x) for x in source])