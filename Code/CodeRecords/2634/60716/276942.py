lists = list(eval(input()))
k = int(input())
order = list()
words = dict()
for i in range(len(lists)):
    for j in range(i+1,len(lists)):
        num = float(lists[i]/lists[j])
        strs = str(lists[i])+'/'+str(lists[j])
        words[num] = strs
        order.append(num)
order.sort()
temp = order[k-1]
string = words.get(num)
templist = string.split('/')
ans = [int(i) for i in templist]
print(ans)