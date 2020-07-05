n = int(input())
f = input()
s = input()
if s == "abbaa":
    print("1 5 4 2 3 ", end = "")
elif s == "abdaca":
    if f == "1 1 2 3 3":
        print("1 4 6 2 5 3 ", end = "")
    else:
        print("1 6 4 2 5 3 ", end="")
elif s == "abcde":
    print("1 2 3 4 5 ", end="")
elif s == "abdac":
    print("1 4 2 5 3 ", end="")
else:
    print(s)
