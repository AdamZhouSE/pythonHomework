def cut(r):
    a = r*r
    count = 0
    for i in range(1,r):
        for j in range(1,r):
            if i*i+j*j <= a:
                count+=1
    return count
T = int(input())
for i in range(T):
    R = int(input())
    print(cut(2*R))