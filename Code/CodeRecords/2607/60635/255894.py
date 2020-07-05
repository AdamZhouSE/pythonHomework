cases=int(input())
for n in range(cases):
    zeros = ones = twos = ans = 0
    hmap = {}
    hmap[(0,0)] = 1
    for i in input():
        if i =='0': 
            zeros += 1
        elif i =='1': 
            ones += 1
        else: 
            twos += 1
        tup = ones-zeros,ones-twos
        if tup in hmap:
            ans += hmap[tup]
            hmap[tup] += 1
        else: 
            hmap[tup] = 1
    print(ans)