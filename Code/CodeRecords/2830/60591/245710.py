b,k = list(map(int,input().split(" ")))
a = list(map(int,input().split(" ")))
ord = 1

for x in range(len(a)):
    if(a[x]*pow(b,k - 1 - x) % 2 != 0):
        ord = 1 - ord
if(ord == 1):
    print("even")
else:
    print("odd")