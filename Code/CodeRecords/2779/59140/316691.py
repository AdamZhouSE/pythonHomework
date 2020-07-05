t = int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().split(" ")]
    for i in range(1,max(arr)+1):
        if (min(arr)*i)%max(arr)==0:
            print(min(arr)*i)
            break