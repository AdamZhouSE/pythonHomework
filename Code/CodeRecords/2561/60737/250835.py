n = int(input())
cond = [int(n) for n in input().split( )]
size = cond[0]
x = cond[1]
mat1 = []
mat2 = []
n = size
while n:
    temp = [int(n) for n in input().split(' ')]
    for i in temp:
        mat1.append(i)
    n -= 1
n = size
while n:
    temp = [int(n) for n in input().split(' ')]
    for i in temp:
        mat2.append(i)
    n -= 1
count = 0
for i in range(size*size):
    for j in range(size*size):
        if mat1[i] + mat2[j] == x:
            count += 1
print(count)