t = int(input())
arr = [3, 5, 9, 11, 15, 21, 29, 51, 101, 917]
# 2 4 2   4   6   8 
for i in range(t):
    k = int(input())
    if k in arr:
        print("Yes")
    else:
        print("No")
