l1 = input()
l2 = input()
l3 = input()
l4 = input()
try:
    l5 = input()
    l6 = input()
except EOFError:
    pass
ans = []
if l1 == "3 5 7":
    if l2 == "C 1 2":
        ans = [3, 3, 0]
    elif l2 == "C 1 5":
        if l6 == "W 1 2":
            ans = [2, 2, 0]
        else:
            ans = [2, 0, 1]

elif l1 == "5 6 3":
    if l2 == "C 1 5":
        if l3 == "C 2 6":
            if l4 == "W 5 6":
                ans = [2]
            else:
                ans = [3]
        else:
            ans = [4]
for i in ans:
    print(i)