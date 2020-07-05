total = int(input())
page = input().split(' ')
for i in range(0,total):
    page[i] = int(page[i])
res = 0
max = page[0]
for i in range(0,total):
    if max > i+1:
        continue
    else:
        res+=1
        if i<total-1 and page[i+1]>max:
            max = page[i+1]
print(res)