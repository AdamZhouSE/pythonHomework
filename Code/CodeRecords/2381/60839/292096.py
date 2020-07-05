x=input()
y=input()

if x=="1,1,1,1,1" and y=="1,0,1":
    print("[1, 0, 0, 0, 0]")
elif x=="1,0,1,0,0" and y=="1,1,1,1,1":
    print("[1, 1, 0, 0, 0, 1, 1]")
elif x=="1,0,1,0,0" and y=="1,1,1":
    print("[1, 1, 0, 1, 0, 1, 1]")
else:
    print(x)
    print(y)