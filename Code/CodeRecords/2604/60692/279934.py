import bisect
list1 = input()[2:-2].split("\", \"")
target = input()
i = bisect.bisect(list1, target)
print(list1[i % len(list1)])