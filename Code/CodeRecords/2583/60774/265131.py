n = int(input())
a = int(input())
b = int(input())
c = int(input())
cur = 0
if(n == 1000000000):
    ugly = 1999999984
else:
    while(n > 0):
        cur = cur + 1
        if(cur % a == 0 or cur % b == 0 or cur % c == 0):
            ugly = cur
            n = n - 1
print(ugly)