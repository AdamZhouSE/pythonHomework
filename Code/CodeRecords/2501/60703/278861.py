n = int(input())
initial = input().split(" ")
messed = input().split(" ")
l =len(initial)
res = 0
for i in range(l-1):
    name1 = initial[i]

    for j in range(i+1,l):
        name2 = initial[j]
        messedIdx1 = messed.index(name1)
        messedIdx2 = messed.index(name2)
        if(messedIdx2-messedIdx1<0):
            res+=1

print(res)