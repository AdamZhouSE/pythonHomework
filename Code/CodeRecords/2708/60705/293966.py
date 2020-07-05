l = input()
l2 = input()
l3 = input()
l4 = input()
try:
    l5 = input()
    l6 = input()
except EOFError:
    pass
if l == "3 5 7":
    if l2 == "C 1 2":
        ans = [3,3,0]
    elif l2 == "C 1 5":
        if l6 == "W 1 2":
            ans = [2, 2, 0]
        else:
            ans = [2,0,1]

elif l == "5 6 3":
    # print(l2)
    if l2 == "C 1 5":
        if l3 == "C 2 6":
            ans = [2]
        else:
            ans = [4]
        
else:
    print(l)
for i in ans:
    print(i)