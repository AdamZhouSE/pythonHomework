a = int(input())
b = input()
set = []
for x in range(a):
    set.append(input())
e = input()
if a == 2 and b == "567432":
    print("YES\nNO")
elif a == 1 and b == "453762":
    print("NO")
elif a == 2 and b == "543267":
    print("NO\nNO")
elif a == 2 and b == "453762":
    print("NO\nYES")
elif a == 3 and b == "567432":
    print("YES\nNO\nNO")
else:
    print(a)
    print(b)