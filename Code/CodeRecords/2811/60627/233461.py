# 2
inp = input()
p,n = inp.split(' ')
p = int(p)
n = int(n)

insert = []
for i in range(n):
    intp = input()
    insert.append(int(intp)%p)

conflict = False
for i,num in enumerate(insert):
    if num in insert[:i]:
        print(i+1)
        conflict = True
        break
if conflict == False:
    print('-1')