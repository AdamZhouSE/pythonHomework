T = int(input())

for t in range(T):
    all = input().split(' ')
    sizea = int(all[0])
    sizeb = int(all[1])
    x = int(all[2])
    a1 = [int(n) for n in input().split(' ')]
    a2 = [int(n) for n in input().split(' ')]

    a1.sort()
    a2.sort()

    for i in range(sizea):
        for j in range(sizeb):
            if a1[i] + a2[j] == x:
                print(a1[i],a2[j])

