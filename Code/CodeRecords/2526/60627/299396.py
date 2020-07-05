s1 = input()
s2 = input()
try:
    arr1 = eval(s1)
except:
    null = 0
    arr1 = eval(s1)
    arr1.pop(arr1.index(0))
arr2 = eval(s2)
re = arr1+arr2
re.sort()
print(re)