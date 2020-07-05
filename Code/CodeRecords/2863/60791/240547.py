num, high = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
for i in range(len(a)):
    if(a[i] > high):
        num+=1
print(num)