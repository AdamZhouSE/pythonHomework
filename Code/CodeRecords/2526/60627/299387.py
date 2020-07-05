s1 = input()
s2 = input()
try:
    arr1 = eval(s1)
except:
    print(s1)
    print(s2)
arr2 = eval(s2)
re = arr1+arr2
re.sort()
print(re)