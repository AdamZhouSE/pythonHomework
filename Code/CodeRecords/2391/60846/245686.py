n=int(input())
map={}
for i in range(n):
    map[input()]=0
k=int(input())
for i in range(k):
    name=input()
    if map.get(name)==None:
        print('WRONG')
    elif map.get(name)==0:
        map[name]=1
        print('OK')
    elif map.get(name)==1:
        print('REPEAT')