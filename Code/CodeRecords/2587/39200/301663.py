n = int(input())
A = []
for x in range(0, n):
    A.append(input())
def cal(a, b):
    x1 = int(a[0])
    y1 = int(a[1])
    x2 = int(b[0])
    y2 = int(b[1])
    delx = abs(x2 - x1)
    dely = abs(y2 - y1)
    return min(delx, dely) + abs(delx - dely)
index = 0
count = 0
while index < len(A)-1:
    count += cal(A[index].split(","), A[index+1].split(","))
    index += 1
print(count)
