n = int(input())
a = bin(n)
if a[-1]== '0' and a[-2] == '0':
    print("True")
else:
    print("False")