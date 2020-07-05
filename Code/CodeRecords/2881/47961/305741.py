a=int(input())
mid=a//2+1

for i in range(1,a+1):
    if i<mid:
        for j in range(1,a+1):
            if j<=mid-i:
                print("*",end="")
            elif j>=mid+i:
                print("*",end="")
            else:
                print("D",end="")
    elif i==mid:
        for j in range(1,a+1):
            print("D",end="")
    else:
        for j in range(1,a+1):
            k=a-i+1
            if j<=mid-k:
                print("*",end="")
            elif j>=mid+k:
                print("*",end="")
            else:
                print("D",end="")
    print()