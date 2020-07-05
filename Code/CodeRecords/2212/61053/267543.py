import math
def divisor_sum(n):
    sum = 0
    for i in range(1,math.ceil(n**(1/2))):
        if n % i == 0:
            sum += i
            if i**2 != n:
                sum += n/i
    sum = int(sum)
    return sum

def Notenougn(n):
    if divisor_sum(n) < 2*n:
        return True
    else:
        return False

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        ans.append(Notenougn(n))
    for res in ans:
        if res:
            print(1)
        else:
            print(0)