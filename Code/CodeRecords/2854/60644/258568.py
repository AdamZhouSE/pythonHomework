arr=input().split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
leg=arr[0]
animal=False
for i in range(0,6):
    if arr.count(arr[i])>=4:
        animal=True
        leg=arr[i]
        break
if not animal:
    print('Alien')
else:
    for i in range(0,4):
        arr.remove(leg)
    if arr[0]!=arr[1]:
        print('Bear')
    else:
        print('Elephant')
