height=int(input())
nodes=input().split(' ')
nodes=list(map(int,nodes))
depth=int(input())
start=pow(2,depth-1)-2+1
end=pow(2,depth)-2
if start>=len(nodes):
    print('EMPTY')
else:
    if end >= len(nodes):
        end = len(nodes) - 1
    result=nodes[start:end+1]
    rStr=''
    for node in result:
        rStr+=str(node)+' '
    print(rStr[:-1])