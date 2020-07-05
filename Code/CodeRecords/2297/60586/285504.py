def t1():
    n=int(input())
    x=input().split(" ")
    node=[]
    for item in x:
        node.append(int(item))
    d = int(input())
    string=''
    for i in range(2**(d-1)-1,n):
        string=string+" "+str(node[i])
    print(string[1:])
t1()