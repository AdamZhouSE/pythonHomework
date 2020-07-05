tests = int(input())
for i in range(0,tests):
    lent = int(input())
    ls = input().split(' ')
    setn = list(set(ls))
    index = ""
    maxx = 0
    for j in range(0,len(setn)):
        tem = ls.count(setn[j])
        if tem == maxx:
            if index > setn[j]:
                index = setn[j]
        elif tem > maxx:
            index = setn[j]
            maxx = tem
    print(index,maxx)