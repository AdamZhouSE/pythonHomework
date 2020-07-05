n = int(input())
for i in range(n):
    w = int(input())
    if w % 2 ==0:
        print(int(pow(2, w/2)))
    else:
        print(int(pow(2, w/2)) * (int(w/2) + 1) - int(w/2)) 