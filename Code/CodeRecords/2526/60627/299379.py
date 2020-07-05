s1 = input()
s2 = input()
if s1 == "[null]":
    print('aaa')
arr1 = eval(s1)
arr2 = eval(s2)
re = arr1+arr2
re.sort()
print(re)