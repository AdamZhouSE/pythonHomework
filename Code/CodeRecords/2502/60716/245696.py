num = int(input())
lists = list()
for i in range(num):
    a = int(input())
    lists.append(a)
price = 0
setli = list(set(lists))
setli.sort()
for i in range(len(setli)):
    temp = setli[i]
    for j in range(len(lists)):
        if lists[j]==temp:
            if j==0:
                price+=lists[j+1]
                lists.pop(j)
            elif j==len(lists)-1:
                price+=lists[j-1]
                lists.pop(j)
            else:
                x = lists[j-1]
                y = lists[j+1]
                if x<=y:
                    price+=x
                    lists.pop(j-1)
                else:
                    price+=y
                    lists.pop(j+1)
print(price)