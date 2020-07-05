
m = input()
n = input()
if m == "":
    root2 = eval(n)
    print(list(sorted(root2)))
if n == "":
    root1 = eval(n)
    print(list(sorted(root1)))
root1 = eval(m)
root2 = eval(n)
print(list(sorted(root1 + root2)))
