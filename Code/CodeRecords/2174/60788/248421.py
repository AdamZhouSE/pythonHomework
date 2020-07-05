from sys import stdin

def match1(line):
    return len(line.split(' '))==4

def match2(line):
    return len(line.split(' '))==3 and line.split(' ')[0]=='1'

def match3(line):
    return len(line.split(' '))==3 and line.split(' ')[0]=='2'

def find_dangerous_path(s,x,y):
    m=[-1]*len(s)
    current=[x]
    inner=[]
    while True:
        new_current=[]
        for i in current:
            for j in find_adjacent(s,i):
                if j not in inner+current:
                    m[j]=max(s[i][j],m[i])
                    new_current.append(j)
                    
        inner+=current
        current=new_current
        if len(current)==0:
            break
    return m[y]


def find_adjacent(s,i):
    t=[]
    for j in range(len(s)):
        if s[i][j]!=0:
            t.append(j)
            
    return t

    

line1=stdin.readline()
num=int(line1.split(' ')[0])
case=int(line1.split(' ')[1])
s=[[0]*num for i in range(num)]
for i in range(case):
    line=stdin.readline()
    if match1(line):
        x=int(line.split(' ')[1])
        y=int(line.split(' ')[2])
        danger=int(line.split(' ')[3])
        s[x][y]=danger
        s[y][x]=danger
    if match2(line):
        x=int(line.split(' ')[1])
        y=int(line.split(' ')[2])
        s[x][y]=0
        s[y][x]=0
    if match3(line):
        x=int(line.split(' ')[1])
        y=int(line.split(' ')[2])
        print(find_dangerous_path(s,x,y))