n = int(input())
while len(str(n)) > 1:
    s = list(str(n))
    n = 0
    for i in s:
        n += int(i)*int(i)
if n == 1:
    print("True")
else:
    print("False")