t = int(input())
for i in range(t):
    n = int(input())
    li = list(input().split())
    temp = ''.join(li)
    temp2 = list(map(int, temp))
    if sum(temp2) % 3 == 0:
        print(1)
    else:
        print(0)
    
