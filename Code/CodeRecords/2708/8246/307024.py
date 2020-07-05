import random
n,m,q = input().split()
nums = (int(n)+1)*[0]  #每个人
where = (int(n)+1)*[0]  #当前每个人在哪个房间
s = set()
dict = dict()  #存入不增加实验信息点的组合情况 
xor = (int(m)+1)*[0] #每个房间的异或值 实际上相当于人的组合异或值 注意同一数两次异或抵消
roomPeople = (int(m)+1)*[0] #当前房间的人数 是从1开始的
for i in range(int(n)+1)[1:]:
    nums[i] = int(random.random()*random.random()*12345)
    roomPeople[1] = roomPeople[1]+1
    xor[1] = xor[1]^nums[i] #初始时3个人都在1号房间
    where[i] = 1
s.add(1)
for i in range(int(q)):
    op, x, y = input().split()
    x = int(x)
    y = int(y)
    if op == 'C':
        if where[x] == y: #这个人已经在y房间
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
                dict[xor[i]] = 1  #把这次计算实验的信息点的不同组合标记为已试验过
                exp = exp + roomPeople[i]
                r.append(i)
        for a in r:
            s.discard(a)
        print(exp)