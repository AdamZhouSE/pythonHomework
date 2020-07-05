length=int(input())
laptops=[]
for i in range(length):
    laptops.append([int(x) for x in input().split()])
laptops.sort(key=lambda x:x[0])
judge=True
for i in range(length-1):
    if laptops[i][1]>laptops[i+1][1]:
        judge=False
        break
if judge:
    print("Poor Alex")
else:
    print("Happy Alex")