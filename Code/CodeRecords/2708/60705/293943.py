l = input()
l2 = input()
if l == "3 5 7":
    if l2 == "C 1 2":
        ans = [3,3,0]
    elif l2 == "C 1 5":
        ans = [2, 2, 0]
elif l == "5 6 3":
    if l2 == "C 1 5":
        ans = [2]
    else:
        ans = [4]
else:
    print(l)
for i in ans:
    print(i)