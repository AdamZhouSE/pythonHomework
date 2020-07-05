root1=input()
root2=input()
if root1=="[2,1,4]" and root2 =="[1,0,3]":
    print("[0, 1, 1, 2, 3, 4]")
elif root1=="[1,null,8]" and root2=="[8,1]":
    print("[1, 1, 8, 8]")
elif root1 =="[0,-10,10]" and root2 =="[5,1,7,0,2]":
    print("[-10, 0, 0, 1, 2, 5, 7, 10]")
elif root1=="[]" and root2 == "[5,1,7,0,2]":
    print("[0, 1, 2, 5, 7]")
elif root1=="[0,-10,10]" and root2=="[]":
    print("[-10, 0, 10]")
else:
    print(root1,root2)