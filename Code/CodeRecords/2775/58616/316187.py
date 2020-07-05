def checksum(n):
    if n % 3 == 0: 
        print(int(n / 3 - 1),int(n / 3),int(n / 3 + 1)) 
    else: 
        print("-1")


for i in range(int(input())):
    n = int(input())
    checksum(n)