# [int(i) for i in input().split(" ")]
a = [int(i) for i in input().replace("[","").replace("]","").replace(","," ").split(" ")]
b = []
for i in a:
    if i%2==0:
        b.append(i)
for i in a:
    if i%2!=0:
        b.append(i)
print(b)
