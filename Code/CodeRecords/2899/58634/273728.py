n = int(input())
a = bin(n)[2:]
if a.count('0')%2 == 0:
    print("true")
else:
    print("false")