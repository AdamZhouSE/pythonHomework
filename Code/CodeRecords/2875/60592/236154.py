total = int(input())
kids = input().split(' ')
res = []
for i in range(0,total):
    for j in range(0,total):
        if int(kids[j]) == i+1:
            res.append(str(j+1))
print(' '.join(res))