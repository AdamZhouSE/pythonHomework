#17
def factorial(num):
    count = 1
    for i in range(1,num+1):
        count *= i
    return count
T = int(input())
for i in range(0,T):
    ori = input().split(" ")
    A = int(ori[0])
    B = int(ori[1])
    n = A + B - 2
    m = max(A,B) -1 
    Cmn = factorial(n) // (factorial(m)*factorial(n-m))
    print(Cmn)
