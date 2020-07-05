aList = [int(i) for i in input().strip('[|]').split(',')]
bList = [int(i) for i in input().strip('[|]').split(',')]
print(sorted(list(set(aList)&set(bList))))