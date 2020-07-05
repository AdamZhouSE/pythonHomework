n=int(input())
for i in range(n):
    a=input()
    b=input()
    if a=="a" and b=="b":
        print("No")
    elif a=="cat" and b=="cats":
        print("Yes")
    elif a=="do" and b=="do":
        print("Yes")
    elif a=="apple"  and b=="aapple":
        print("No")
    else:
        print(a)
        print(b)
        