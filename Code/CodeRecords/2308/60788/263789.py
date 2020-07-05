def f(node_list,root,s):
    
    if node_list[root-1][0]!=0 :
        f(node_list,node_list[root-1][0],s)
    s.append(root)
    if node_list[root-1][1]!=0:
        f(node_list,node_list[root-1][1],s)




line = input().strip()
nums = int(line.split()[0])
roo = int(line.split()[1])
nod_list = [[0, 0] for i in range(20)]
for i in range(nums):
    new_line = input().strip()
    nod_list[int(new_line.split()[0]) - 1][0] = int(new_line.split()[1])
    nod_list[int(new_line.split()[0]) - 1][1] = int(new_line.split()[2])
target= int(input().strip())   
s=[]
f(nod_list,roo,s)
index=s.index(target)
if index==len(s)-1:
    print(0)
else:
    print(s[index+1])