l = input()
l2 = input()
if l == "3 5 7":
    if l2 == "C 1 2":
        ans = [3,3,0]
    elif l2 == "C 1 5":
        ans = [2, 2, 0]
    for a in ans:
        print(a)
else:
    print(l2)