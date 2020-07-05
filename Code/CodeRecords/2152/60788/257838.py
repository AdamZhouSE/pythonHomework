def f(i,value,arrival):
    path=[i+1]
    current=i
    s=value[i]
    while not arrival[current] in path:
        path.append(arrival[current])
        s+=value[arrival[current]-1]
    return s
        

num=int(input().strip())
value=[int(x) for x in input().strip().split()]
arrival=[int(x) for x in input().strip().split()]
for i in range(num):
    print(f(i,value,arrival))