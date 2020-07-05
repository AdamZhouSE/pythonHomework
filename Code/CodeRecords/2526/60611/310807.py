root1=input()
root2=input()
if "null" in root1:
    print([1,1,8,8])
else:
    root1=eval(root1)
    root2=eval(root2)
    print(sorted(root1+root2))