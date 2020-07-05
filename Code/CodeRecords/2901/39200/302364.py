n = int(input())
n1 = n << 1
result = n & n1
if result == 0 or result == 1:
    print("True")
else:
    print("False")
