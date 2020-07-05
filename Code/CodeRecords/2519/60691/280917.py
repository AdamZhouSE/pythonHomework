import itertools


def istriangle(l):
    l.sort()
    if int(l[0]) + int(l[1]) > int(l[2]):
        return True
    return False


def perimeter(l):
    return int(l[0])+int(l[1])+int(l[2])


s = input()
s = s.strip('[]')

l = s.split(',')

lcombination = list(itertools.combinations(l, 3))

nums = []
for i in range(len(lcombination)):
    if istriangle(list(lcombination[i])):
        nums.append(perimeter(list(lcombination[i])))

if len(nums) == 0:
    print(0)
else:
    print(max(nums))