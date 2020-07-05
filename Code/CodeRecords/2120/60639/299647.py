import math
number=int(input())
n=int(math.sqrt(number))
tail=n+(number%n!=0)
pro=1
for i in range(n-1):
    pro*=n
pro*=tail
print(pro)