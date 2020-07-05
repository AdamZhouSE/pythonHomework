input()
nums = list(map(int,input().split(" ")))
count = 0
ords = []
for num in nums:
    if(num%2 == 0):
        count += num
    else:
        ords.append(num)
if(len(ords)%2==1):
    ords.sort()
    count += sum(ords)
    count -= ords[0]
else:
    count += sum(ords)
print(count)