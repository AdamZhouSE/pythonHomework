t = int(input())
for i in range(0,t):
    s = input().split(' ')
    L = int(s[0])
    R = int(s[1])
    if(R >= 10):
        print((10 - L) + int(R / 11))
    else:
        print(R - L + 1)
    
    