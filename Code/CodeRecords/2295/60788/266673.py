line1=input().strip()
node_num=int(line1.split()[0])
root=int(line1.split()[1])-1
s=[[0]*node_num for i in node_num]
for i in range(node_num):
    line=input().strip()
    a=int(line.split()[0])-1
    b=int(line.split()[1])-1
    c=int(line.split()[2])-1
    if b>0:
        s[a][b]=1
        s[b][a]=1
    if c>0:
        s[a][c]=1
        s[c][a]=1

