n = eval(input())
file = eval(input())
U = []
for i in range(n):
    U.append(eval(input()))
U.sort(reverse=True)
count = 0
index = 0
while file>0:
    file = file - U[index]
    index = index + 1
    count = count + 1
print(count)