aList, k = [int(i) for i in input().strip('[|]').split(',')], int(input())
print(sorted(aList, reverse=True)[k-1])