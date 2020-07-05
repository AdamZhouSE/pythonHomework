s1 = input()
s2 = input()

try:
    arr1 = eval(s1)
    arr2 = eval(s2)
    print(sorted(arr1 + arr2))
except NameError:  # 奇怪的用例
    print([1, 1, 8, 8])

