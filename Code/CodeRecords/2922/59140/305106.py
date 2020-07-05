n=int(input())
arr = [int(x) for x in input().split(" ")]
if len(set(arr))<=3:print("YES")
else:print("NO")