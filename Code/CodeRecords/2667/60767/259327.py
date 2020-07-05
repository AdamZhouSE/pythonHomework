def ans(bits,n):
    return 2**bits-n

numOfTests = int(input())
for t in range(numOfTests):
    temp = input().split()
    n = int(temp[0])
    bits = int(temp[1])
    print(ans(bits,n))
