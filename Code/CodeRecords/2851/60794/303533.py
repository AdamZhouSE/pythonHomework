num = int(input())
dot = []
for i in range(num):
    dot.append(input().split(" "))
largest = 0
for i in range(num):
    if int(dot[i][0]) + int(dot[i][1]) > largest:
        largest = int(dot[i][0]) + int(dot[i][1])
print(largest)