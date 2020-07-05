T = int(input())
source = []
for x in range(0,T):
    source.append(int(input()))
for x in range(0,T):
    R = source[x]
    count = 0
    for a in range(1,2*R):
        for b in range(1,2*R):
            if a*a+b*b<4*R*R:
                count = count+1
    print(count)