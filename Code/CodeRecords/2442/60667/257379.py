li = eval(input())
if len(li) < 2:
    print(0)
    quit()
li.sort()
maxi = 0
for i in range(len(li)-1):
    if li[i+1] - li[i] > maxi:
        maxi = li[i+1] - li[i]
print(maxi)        