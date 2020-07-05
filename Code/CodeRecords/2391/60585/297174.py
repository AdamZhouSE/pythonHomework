n=eval(input())
name=[]
for _ in range(n):
    name.append(input())
visited=[0 for i in range(n)]
m=eval(input())
for _ in range(m):
    temp=input()
    if temp not in name:
        print('WRONG')
    else:
        m=name.index(temp)
        if visited[m]==0:
            print('OK')
            visited[m]=1
        else:
            print('REPEAT')