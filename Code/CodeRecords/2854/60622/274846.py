arr=list(map(int,input().split()))
for x in arr:
    if arr.count(x)>=4:
        for m in range(4):
            arr.remove(x)
print(arr)
if len(arr)!=2:
    print("Alien")
elif arr[0]==arr[1]:
    print("Elephant")
else:
    print("Bear")


