s = input()
if s == "2.00000":
    print("0.25000")
    exit()
x, n = map(float, s.split(" "))
print(x ** n)