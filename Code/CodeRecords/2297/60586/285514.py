def t1():
    n=int(input())
    x=input().split(" ")
    node=[]
    for item in x:
        node.append(int(item))
    d = int(input())
    string=''
    if(n<=2**(d-1)-1):
        print("EMPTY")
        return ;
    if 2**d-1>n:
        end=n
    else:
        end=2**d-1
    for i in range(2**(d-1)-1,end):
        string=string+" "+str(node[i])
    print(string[1:])
t1()