def breakDown(num):
    if(num < 12):
        return [num]
    else:
        return breakDown(int(num / 2)) + breakDown(int(num / 3)) + breakDown(int(num / 4))
    
t = int(input())
for i in range(0,t):
    num = int(input())
    print(sum(breakDown(num)))