import ast
lists1 = ast.literal_eval(input())
lists2 = ast.literal_eval(input())

set1 = set(lists1)
set2 = set(lists2)

longerOne = []
otherOne = []
if set1.__len__() > set2.__len__():
    longerOne = set1
    otherOne = set2
else:
    longerOne = set2
    otherOne = set1

resSet = longerOne.intersection(otherOne)
lists = list(resSet)
lists.sort()
print(lists)