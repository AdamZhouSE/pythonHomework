row=[int(n) for n in input().split()]
n=row[0]
d=row[1]
num=[int(n) for n in input().split()]
total=0
for index1 in range(len(num)-1):
    for index2 in range(index1+1,len(num)):
        if abs(num[index1]-num[index2])<=d:
            total+=2
print(total)