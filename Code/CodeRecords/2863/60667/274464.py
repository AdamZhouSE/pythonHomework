s = input().split()
n = int(s[0])
h = int(s[1])
width = 0
heights = list(map(int,input().split()))
for i in heights:
    if i > h:
        width+=2
    else:
        width+=1
print(width)