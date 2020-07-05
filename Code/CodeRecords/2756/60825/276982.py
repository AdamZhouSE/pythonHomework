def shortestAlternatingPaths(n, red_edges, blue_edges):
    red_path = [set() for i in range(n)]
    blue_path = [set() for i in range(n)]
    dist = [[None, None] for i in range(n)]
    dist[0] = [0, 0]
    step = 0
    now_red = [0]
    now_blue = [0]
    for start, end in red_edges:
        red_path[start].add(end)
    for start, end in blue_edges:
        blue_path[start].add(end)
    while len(now_red) != 0 or len(now_blue) != 0 :
        new_red, new_blue = [], []
        step += 1
        if len(now_blue) != 0:
            for point in now_blue:
                for next_point in red_path[point]:
                    if dist[next_point][0] is None:
                        new_red.append(next_point)
                        dist[next_point][0] = step
        if len(now_red) != 0:
            for point in now_red:
                for next_point in blue_path[point]:
                    if dist[next_point][1] is None:
                        new_blue.append(next_point)
                        dist[next_point][1] = step
        now_red, now_blue = new_red, new_blue
    ans = []
    for i in range(n):
        if dist[i][0] is None and dist[i][1] is None:
            ans.append(-1)
        elif dist[i][0] is not None and dist[i][1] is not None:
            ans.append(min(dist[i][0], dist[i][1]))
        elif dist[i][0] is not None:
            ans.append(dist[i][0])
        else:
            ans.append(dist[i][1])
    return ans

k=int(input())
s=input()
s=s.replace('[','')
s=s.replace(']','')
s=s.replace(',',' ')
l=s.split()
l= list(map(int, l))

d1=[]
for i in range(0, len(l), 2):
    dd=[l[i],l[i+1]]
    d1.append(dd)

s=input()
s=s.replace('[','')
s=s.replace(']','')
s=s.replace(',',' ')
l=s.split()
l= list(map(int, l))

d2=[]
for i in range(0, len(l), 2):
    dd=[l[i],l[i+1]]
    d2.append(dd)

print(shortestAlternatingPaths(k,d1,d2))