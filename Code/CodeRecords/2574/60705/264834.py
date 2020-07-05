prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
n = int(input())
for i in range(0, n):
    num = int(input())
    print(prime[num+1]**2+1)