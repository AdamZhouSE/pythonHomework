n = int(input())
a = [int(i) for i in input().split()]
odd = 0
even = 0
for item in a:
    if(item%2 == 0):
        even += 1
    else:
        odd += 1
if(odd %2 != 0):
    print(odd)
else:
    print(even)