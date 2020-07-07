T = int(input())
for t in range(T):
    l = list(format(int(input()), 'b').zfill(8))
    for i in range(0, len(l)):
        if(i%2 == 0):
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
    print(int(''.join(l), 2))