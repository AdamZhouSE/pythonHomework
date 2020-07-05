n = int(input())
books = [int(x) for x in input().split()]
k = int(input())
targets = [int(x) for x in input().split()]
for i in targets:
    ceil = 1
    for j in books:
        if i>j:
            i-=j
            ceil+=1
        else:
            print(ceil)
            break