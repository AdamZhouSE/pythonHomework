while True:
    try:
        n, r, avg = [int(each) for each in input().split()]
        ab_i = []
        for i in range(n):
            ab_i.append([int(each) for each in input().split()])
        ab_i = sorted(ab_i, key=lambda x: x[1])
        target = n * avg
        current = sum([each[0] for each in ab_i])
        time_total = 0
        if current < target:
            index = 0
            while current < target:
                while ab_i[index][0] >= r:
                    index += 1
                time_total += ab_i[index][1]
                ab_i[index][0] += 1
                current += 1
            print(time_total)
        else:
            print(0)
    except:
        break
 
