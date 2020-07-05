a=int(input())
b=int(input())
c=int(input())
sort_abc = sorted([a, b, c])
a, b, c = sort_abc[0], sort_abc[1], sort_abc[2]
if a+1 == b and b+1 == c:
    print("[0, 0]")
else:
    print([1 if (b-a <= 2 or c-b <= 2) else 2, c-a-2])