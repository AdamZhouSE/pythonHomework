from sys import stdin
def hu_su(a,b):
    return gcd(a,b)==1
    
    
def gcd(a,b):
    if a==1 or b==1:
        return 1
    else:
        if a==b:
            return a
        elif a<b:
            return gcd(a,b-a)
        else:
            return gcd(a-b,b)
        
        
def join(graph1,graph2):
    for i in range(0,len(graph1)):
        for j in range(0,len(graph1)):
            if not (graph1[i][j]==0 and graph2[i][j]==0):
                graph1[i][j]=1
    
def construct_graph(s):
    length=len(s)
    t=[[0]*length for i in range(length)]
    for i in range(length):
        for j in range(length):
            if not hu_su(s[i],s[j]):
                t[i][j]=1
    return t


def f(li):
    if len(li)==1:
        return 1
    else:
        s=li
        t=[x+1 for x in li]
        graph1=construct_graph(s)
        graph2=construct_graph(t)
        join(graph1,graph2)
        max=0
        for i in graph1:
            if i.count(1)>max:
                max=i.count(1)
        return max
        
        
num=int(stdin.readline().strip())
s=[]
for i in range(num):
    s.append(int(stdin.readline().strip()))
print(f(s),end='')
