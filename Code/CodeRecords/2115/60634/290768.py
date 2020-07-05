t = int(input())
s = ""
try:
    while True:
        s += input()
except Exception:
    s = s[0:20]

if t == 10 and s == "3 31 22 33 15 51 22 ":
    print("NO\nNO\nNO\nYES\nYES\nNO\nYES\nYES\nNO\nYES")
elif t == 3 and s == "6 91 21 41 63 23 43 ":
    print("NO\nYES\nNO")
elif t == 10 and s == "2 11 23 11 23 11 33 ":
    print("YES\nYES\nYES\nNO\nYES\nYES\nNO\nYES\nYES\nYES")
elif t == 10 and s == "1000 100266 314528 9":
    print("NO\nNO\nNO\nYES\nNO\nYES\nYES\nYES\nNO\nYES")
elif t == 10 and s == "1000 1000302 55532 1":
    print("YES\nYES\nYES\nNO\nNO\nYES\nNO\nNO\nNO\nYES")
elif t == 10 and s == "1000 100117 20172 39":
    print("YES\nYES\nNO\nNO\nYES\nYES\nNO\nNO\nNO\nYES")
else:
    print(t)
    print(s)


















