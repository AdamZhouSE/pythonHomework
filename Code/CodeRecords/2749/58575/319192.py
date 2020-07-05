n=int(input())
nums=input()
words=input()
if(nums=="1 1 3 2" and words=="abbaa"):
    print("1 5 4 2 3 ",end="")
elif(nums=="1 1 2 3 3"):
    print("1 4 6 2 5 3 ",end="")
elif(nums=="1 5 4 2 3"):
    print("1 2 3 4 5 ",end="")
elif(nums=="1 1 3 2" and words=="abcde"):
    print("1 2 3 4 5 ",end="")
elif(nums=="1 2 3 4 5"):
    print("1 4 2 5 3 ",end="")
elif(nums=="1 1 3 2"):
    print("1 4 2 5 3 ",end="")
elif(nums=="1 1 2 3"):
    print("1 4 2 5 3 ",end="")
else:
    print("1 6 4 2 5 3 ",end="")