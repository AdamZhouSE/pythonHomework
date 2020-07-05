n = int(input())
a = input().split(" ")
d = int(input())
start = 2**(d-1)-1
if n < 2**(d-1):
    print("EMPTY", end="")
elif 2*start > n-1:
    print(a[start], end="")
    for i in range(start + 1, n):
        print(" " + str(a[i]), end="")
else:
    print(a[start], end="")
    for i in range(start+1, start*2+1):
        print(" "+str(a[i]), end="")
print()
