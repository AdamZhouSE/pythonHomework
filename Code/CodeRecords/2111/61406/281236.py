def uglynumber(n):
    while n % 2 == 0:
        n = n / 2
    while n % 3 == 0:
        n = n / 3
    while n % 5 == 0:
        n = n / 5
    if n == 1:
        return True
    else:
        return False


k = int(input())
count = 0
i=1
while True:
    if uglynumber(i):
        count+=1
    if count==k:
        break
    i+=1
print(i)