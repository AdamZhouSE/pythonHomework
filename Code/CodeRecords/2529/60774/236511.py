def initialize(s):
    B = []
    for i in range(0,len(s)):
        B.append(int(s[i]))
        B = sorted(B)
    return B

powerOfTwo = []
power = 1
while(power < 10**9):    
    powerOfTwo.append(initialize(str(power)))
    power = power * 2
A = initialize(input())
if(A in powerOfTwo):
    print('true')
else:
    print('false')