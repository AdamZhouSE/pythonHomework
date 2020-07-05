import copy
class Disjoint_set:
    def __init__(self,n):
        self.li=[[x+1] for x in range(n)]
    def union(self,x,y):
        index1=0
        index2=0
        for i in range(len(self.li)):
            if x in self.li[i]:
                index1=i
            if y in self.li[i]:
                index2=i
        self.li[index1]+=self.li[index2]
        self.li.pop(index2)
    def query(self,x):
        for i in range(len(self.li)):
            if x in self.li[i]:
                return i
        return 0
class Edge:
    def __init__(self,a,b,value):
        self.dot1=a
        self.dot2=b
        self.value=value



def ten_to_three(number):
    num=number
    s=[]
    while num!=0:
        s.append(str(num%3))
        num=int(num/3)
    s.reverse()
    return ''.join([str(x) for x in s])
def three_to_ten(a):
    m=0
    list_a=list(a)
    for k in list_a:
        m*=3
        m+=int(k)
    return m

def add(a,b):
    list_a=list(a)
    list_b=list(b)
    s=[]
    if len(list_a)>len(list_b):
        for i in range(len(list_a)-len(list_b)):
            s.append(list_a.pop(0))
    elif len(list_b)>len(list_a):
        for i in range(len(list_b)-len(list_a)):
            s.append(list_b.pop(0))
    for i in range(len(list_a)):
        s.append(str((int(list_a[i])+int(list_b[i]))%3))
    return ''.join(s)
def do_sum(x):
    m='0'
    for k in x:
        m=add(m,ten_to_three(k.value))
    return three_to_ten(m)

def f(disjoint,edge_li,total_edge):
    if len(edge_li)<total_edge :
        return []
    elif len(edge_li)==0:
        return [[]]
    else:
        first_edge=edge_li.pop(0)
        if disjoint.query(first_edge.dot1)!=disjoint.query(first_edge.dot2):
            set1=f(copy.deepcopy(disjoint),copy.deepcopy(edge_li),total_edge)
            disjoint.union(first_edge.dot1,first_edge.dot2)
            set2 =f(disjoint,edge_li,total_edge-1)
            for every_edges in set2:
                every_edges.append(first_edge)
            return set1+set2
        else:
            return f(disjoint,edge_li,total_edge)

def seek_all_tree(edge_li,total_edge_num):
    if len(edge_li)==0 or len(edge_li)<total_edge_num:
        return []
    disjoint_set=Disjoint_set(total_edge_num+1)
    first_edge=edge_li.pop(0)
    trees1=seek_all_tree(copy.deepcopy(edge_li),total_edge_num)
    disjoint_set.union(first_edge.dot1,first_edge.dot2)
    trees2=f(disjoint_set,edge_li,total_edge_num-1)
    for tree in trees2:
        tree.append(first_edge)
    return trees1+trees2

line1=input().strip()
dot_num=int(line1.split()[0])
edge_num=int(line1.split()[1])
edge_list=[]
for i in range(edge_num):
    line=input().strip()
    edge=Edge(int(line.split()[0]),int(line.split()[1]),int(line.split()[2]))
    edge_list.append(edge)
trees=seek_all_tree(edge_list,dot_num-1)
trees_value=[do_sum(x) for x in trees]
print(sum(trees_value))
