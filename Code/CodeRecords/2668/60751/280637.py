import math
def calculate(num):
    count=0
    while(num!=0):
        num//=2
        count+=1
    return count
        
num=int(input())
for i in range(num):
    N=int(input())
    print(str(int(math.pow(2,calculate(N)))-1-N)+" "+str(int(math.pow(2,calculate(N)))-1))

