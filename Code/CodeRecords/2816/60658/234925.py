n = int(input())
li = [int(x) for x in input().split()]
li.sort()
print(li[int((n-1)/2)])