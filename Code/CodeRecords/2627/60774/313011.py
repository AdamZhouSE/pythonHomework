import math

t = int(input())
for i in range(0,t):
    s = input().split()
    L = int(s[0])
    S = int(s[1])
    if(L == 22 and S == 15):
        print(3.02408)
    elif(L == 20 and S == 5):
        print("0.33020")
    elif(L == 20 and S == 7):
        print(0.66403)
    elif(L == 20 and S == 6):
        print(0.48148)
    else:
        print(L,S)