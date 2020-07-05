length = int(input())
a = [int(i) for i in input().split()]
count = 0
for item in a:
    if(item >= 0):
        count += item
    else:
        count -= item
print(count)
             