root1 = input()
root2 = input()

if root1 =="" or root1=="null":
    root1 = []
else:
    root1 = eval(root1)
if root2 == "" or root2=="null":
    root2 = []
else:
    root2 = eval(root2)


root1.extend(root2)
root1.sort()
print(root1)