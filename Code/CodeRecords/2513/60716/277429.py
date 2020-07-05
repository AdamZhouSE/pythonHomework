num = int(input())
lists = list()
for i in range(num):
    strs = input().split(',')
    temp = [int(t) for t in strs]
    lists.extend(temp)
loc = int(input())
lists.sort()
print(lists[loc-1])