t = int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().split(" ")]
    if max(arr)%min(arr)==0:
        print(max(arr))
    else:print(max(arr)*min(arr))