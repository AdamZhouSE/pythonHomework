n=int(input())
list=[int(i) for i in input().split()]
list.sort()
if n>2:
    if (list[n-1]-list[0])!=(list[n-2]-list[1]):
        print("NO")
    else:
        print("YES")
else:
    print("YES")