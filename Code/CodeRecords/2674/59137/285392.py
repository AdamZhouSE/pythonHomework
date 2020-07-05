def s31():
    t = int(input())
    for i in range(t):
        s = input()
        index_a = []
        index_b = []
        index_c = []

        for x in range(len(s)):
            if s[x] == 'a':
                index_a.append(x)
            elif s[x] == 'b':
                index_b.append(x)
            elif s[x] == 'c':
                index_c.append(x)

        count = 0
        for ia in range(len(index_a)):
            for ib in range(len(index_b)):
                for ic in range(len(index_c)):

                    if index_a[ia] < index_b[ib] < index_c[ic]:
                        a = 1
                        b = 1
                        c = 1

                        for ja in range(ia+1, len(index_a)):
                            if index_a[ja] < index_b[ib]:
                                a += 1
                        for jb in range(ib+1, len(index_b)):
                            if index_a[ia] < index_b[jb] < index_c[ic]:
                                b += 1
                        for jc in range(ic+1, len(index_c)):
                            c += 1

                        count += a * b * c
        print(count)

        
        
s31()