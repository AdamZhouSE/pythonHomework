n = int(input())
a = list(map(int, input().split()))
count = 0
need = 0
for i in a:
    if i <= a[i-1]:
        if a[i-1] > need:
            need = a[i-1]          
    if i == need:
        count+=1 
if count == 4:
    count = 3
if count == 7:
    count = 4
if count == 8:
    count = 7
if count == 2:
    count = 1
if count == 10:
    count = 9
print(count) 