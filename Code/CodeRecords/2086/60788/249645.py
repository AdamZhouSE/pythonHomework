class edge:
    def _init_(start,end,value):
        self.start=start
        self.end=end
        self.value=value

class disjoint_set:
    def _init_(li):
        self.all=li
    def union(index1,index2):
        self.all[index1]+=self.all[index2]
        self.all.pop(index2)
    def check(element):
        for i in self.all:
            if element in i:
                return self.all.index(i)
        return -1
    def add(element):
        self.all.append(element)
        
def find_min(li):
    if len(li)==1:
        return 0
    else:
        index=0
        for i in range(len(li)):
            if li[i].value<li[index].value:
                index=i
        return index
        
line1=input()
dot=int(input().strip().split()[0])
edge=int(input().strip().split()[1])
li=[]
for i in range(edge):
    line=input().strip()
    start=int(line.split()[0])-1
    end=int(line.split()[1])-1
    value=int(line.split()[2])
    e=edge(start,end,value)
    li.append(e)
    
s=[i for i in range(dot)]
dis=disjoint_set(s)
tree=[]
for j in range(dot-1):
    index=find_min(li)
    edge_under_check=li[index]
    start=edge_under_check.start
    end=edge_under_check.end
    if dis.check(start)!=dis.check(end):
        tree.append(edge_under_check)
        li.pop(index)
        dis.union(dis.check(start),dis.check(end))
    else:
        li.pop(index)
            
total_weight=0
for k in tree:
    total+=k.value
        
    