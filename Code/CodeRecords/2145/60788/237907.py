from sys import stdin
def min(li):
    min=li[0]
    for i in li:
        if i<min:
            min=i
    return min

    
num=int(stdin.readline().strip())
for i in range(0,num):
    length=int(stdin.readline().strip())
    graph=[int(x) for x in stdin.readline().split()]
    max=0
    for j in range(1,length+1):
        for k in range(0,length-j+1):
            width=min(graph[k:k+j])
            S=j*width
            if S>max:
                max=S
                
    print(max)
