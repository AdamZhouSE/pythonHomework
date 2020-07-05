string = "".join(input().split(" "))
res = 0
if "0" <= string[0] <= "9" or string[0] == "-":
    zero = 0
    if string[0] == "-":
        zero = 1
    for i in range(zero, len(string)):
        if not "0" <= string[i] <= "9":
            string = string[:i]
            break
    res = int(string)
if not -pow(2,31) <= res :
    res = -2147483648
if not res <= pow(2,31)-1:
    res = 2147483647
print(res)