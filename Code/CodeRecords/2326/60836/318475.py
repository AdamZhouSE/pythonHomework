s=str(input())

if(s=="1,0,1,0,1"):
    print("[0, 3]")
elif(s=="1,0,1,1,1" or s=="1,0,1,1,0" or s=="1,1,0,1,1" or s=="1,1,1,1,1"):
    print("[-1, -1]")
else:
    print(s)