n = int(input())
a = [int(i) for i in input().split()]
odd, even = 0,0
for item in a:
    if(item%2 == 0):
        even += item
    else:
        odd += item
if(odd > even):
    print(odd)
else:
    print(even)