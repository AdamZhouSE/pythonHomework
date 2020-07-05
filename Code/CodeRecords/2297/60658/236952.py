n = int(input())
nodes = input().split()
d = int(input())
upper = 0
lower = 0
for i in range(1,d+1):
    upper+=2**(i-1)
    if i == d-1:
        lower = upper
end = min(upper,n)
if lower<=end:
    print(" ".join(nodes[lower:end]))
else:
    print("EMPTY")