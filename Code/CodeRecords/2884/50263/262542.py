n,d = input().split()
n = int(n)
d = int(d)
list = input().split()
count = 0
for i in range(n):
    for j in range(n):
        if i != j and (abs(int(list[i])-int(list[j])) < d or abs(int(list[i])-int(list[j])) == d):
            count+=1
print(count)
            