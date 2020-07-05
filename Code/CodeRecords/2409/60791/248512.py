a = [int(i) for i in input().split(',')]
odd,even = 0,0
for item in a:
    if(item%2 == 0):
        even +=1 
    else:
        odd += 1
if(odd>even):
    print(even)
else:
    print(odd)