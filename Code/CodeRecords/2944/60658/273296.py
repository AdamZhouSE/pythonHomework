s = input()
stack = 0
for i in s:
    if i=="(":
        stack+=1
    elif i==")":
        if stack:
            stack-=1
        else:
            print("NO")
            exit()
print("YES" if stack==0 else "NO",end="")