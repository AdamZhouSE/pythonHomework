def que(x):
    sum = 0
    for i in s.values():
        if x*i[0]+i[1]>i[2]:
            sum+=1
    return sum
    
    
def add(a,b,c):
    s[index]=tuple([a,b,c])

    
def delate(i):
    del s[i]

    
index = 0
s = {}
n = int(input())
for i in range(n):
    li = input().split()
    if li[0]=='Add':
        index+=1
        add(int(li[1]),int(li[2]),int(li[3]))
        
    elif li[0]=='Query':
        print(que(int(li[1])))
    elif li[0]=='Del':
        delate(int(li[1]))