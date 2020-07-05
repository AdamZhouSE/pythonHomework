x = input()
li = list(eval(x))
import collections

c = collections.Counter(li)
for i in c.items():
    if i[1] == 1:
        print(i[0])
        break
