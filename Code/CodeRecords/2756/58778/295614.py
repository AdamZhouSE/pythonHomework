def shortestAlternatingPaths(n,red_edges,blue_edges):
    #其中red_path[i]是以i点为起点的红边的终点的集合
    red_path=[set() for i in range(n)]
    blue_path=[set() for i in range(n)]
    #dist[i][0]表示从0到i‘路径a’的最短距离，dist[i][1]表示从0到i‘路径b’的最短距离
    #‘路径a’表示红蓝红，‘路径b’表示蓝红蓝
    dist=[[None,None] for i in range(n)]
    dist[0]=[0,0]
    step=0
    #表示现在红色可以到达的地方
    now_red=[0]
    now_blue=[0]
    for start,end in red_edges:
        red_path[start].add(end)
    for start,end in blue_edges:
        blue_path[start].add(end)

    #找到分别以红边开始和以蓝边开始的两条最短路径
    while len(now_red) != 0 or len(now_blue) != 0:
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
    ans=[]
    #在这两条最短路径中选择小的
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
n=int(input())
red_edges=eval(input())
blue_edges=eval(input())
print(shortestAlternatingPaths(n,red_edges,blue_edges))