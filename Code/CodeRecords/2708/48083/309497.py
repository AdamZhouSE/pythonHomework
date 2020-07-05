import random
n,m,q = input().split()
nums = (int(n)+1)*[0]  
where = (int(n)+1)*[0]  
s = set()
dict = dict()  
xor = (int(m)+1)*[0] 
roomPeople = (int(m)+1)*[0]
for i in range(int(n)+1)[1:]:
    nums[i] = int(random.random()*random.random()*12345)
    roomPeople[1] = roomPeople[1]+1
    xor[1] = xor[1]^nums[i] 
    where[i] = 1
s.add(1)
for i in range(int(q)):
    op, x, y = input().split()
    x = int(x)
    y = int(y)
    if op == 'C':
        if where[x] == y: 
            continue
        s.discard(where[x])
        s.discard(y)
        xor[where[x]] = xor[where[x]]^nums[x]
        roomPeople[where[x]] = roomPeople[where[x]]-1
        if dict.get(xor[where[x]]) != 1:  
            s.add(where[x])
        xor[y] = xor[y] ^ nums[x]
        roomPeople[y] = roomPeople[y]+1
        if dict.get(xor[y]) != 1:
            s.add(y)
        where[x] = y
    elif op == 'W':
        exp = 0
        r = []
        for i in s:
            if i>=x and i<=y:
                dict[xor[i]] = 1  
                exp = exp + roomPeople[i]
                r.append(i)
        for a in r:
            s.discard(a)
        print(exp)