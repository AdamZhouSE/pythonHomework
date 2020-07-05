a = input()
b = a.split(" ")
n = int(b[0])
d = int(b[1])
heights = [int(i) for i in input().split(" ")]
num = 0
for i in range(0,n-1):
    for j in range (i+1,n):
        if abs(heights[i]-heights[j])<=d:
            num += 2
print(num)
