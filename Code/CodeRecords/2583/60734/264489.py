n = int(input())
a = int(input())
b = int(input())
c = int(input())

count = 0
i = 1
while count < n:
    i+=1
    if i%a == 0 or i%b == 0 or i%c == 0:
        count+=1
print(i)