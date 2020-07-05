an,bn = input().split(" ")
k,m = input().split(" ")

a = input().split(" ")
b = input().split(" ")

a.sort()
b.sort()

if(int(a[int(k)])<int(b[int(bn)-int(m)])):
    print("YES")
else:
    print("NO")