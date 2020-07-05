num = int(input())
lists = list()
for i in range(num):
    a = int(input())
    lists.append(a)
alist = lists.copy()
price = 0
setli = list(set(lists))
setli.sort()
for i in range(len(setli)-1):
    temp = setli[i]
    while True:
        if lists.count(temp)==0:
            break
        j = lists.index(temp)
        if lists[j]==temp:
            if j==0:
                price+=lists[j+1]
            elif j==len(lists)-1:
                price+=lists[j-1]
            else:
                x = lists[j-1]
                y = lists[j+1]
                if x<=y:
                    price+=x
                else:
                    price+=y
        lists.pop(j)
if price==0:
    print(alist)
print(price)