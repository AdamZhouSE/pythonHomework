n=eval(input())
for i in range(1,int(n/2)+1):
    for j in range(int((n+1)/2)-i):
        print("*", end="")
    for k in range(2*i-1):
        print("D", end="")
    for j in range(int((n+1)/2)-i):
        print("*", end="")
    print()
for i in range(n):
    print("D",end="")
print()
for i in range(int(n/2),0,-1):
    for j in range(int((n+1)/2)-i):
        print("*", end="")
    for k in range(2*i-1):
        print("D", end="")
    for j in range(int((n+1)/2)-i):
        print("*", end="")
    print()