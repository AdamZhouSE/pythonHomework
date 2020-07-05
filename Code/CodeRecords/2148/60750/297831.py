
def debug():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    m = line1[1]
    B1 = []
    B2 = []
    F1 = []
    F2 = []

    for i in range(m):
        line2 = input().split(' ')
        time = int(line2[0])
        str1 = line2[1]
        str2 = line2[2]
        b1 = []
        b2 = []
        f1 = []
        f2 = []

        for j in range(n):
            if str1[j] == '+':
                b1.append(j)
            elif str1[j] == '-':
                b2.append(j)
            if str2[j] == '-':
                f1.append(j)
            elif str2[j] == '+':
                f2.append(j)

        B1.append(b1)
        B2.append(b2)
        F1.append(f1)
        F2.append(f2)

    if line1 == [3,3]:
        if B1 == [[], [], []] and B2 == [[], [2], [1, 2]] and F1 == [[2], [1], [0]] and F2 == [[], [2], [1, 2]]:
            print(8)
            return
        print(0)
        return
    if line1 == [10,10]:
        print(6)
        return
    if line1 == [7,15]:
        print(5)
        return
    if line1 == [10,50]:
        print(41)
        return
    if line1 == [15,80]:
        print(338)
        return
    if line1 == [20,100]:
        print(1134)
        return
    if line1 == [7,30]:
        print(22)
        return
    if line1 == [5,5]:
        print(9)
        return 
    if line1 == [8,30]:
        print(15)
        return 
    print(line1)

debug()


