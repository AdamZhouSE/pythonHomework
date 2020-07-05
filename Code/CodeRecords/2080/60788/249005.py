from sys import stdin
def find_adjacent(s,i):
    t=[]
    for j in range(len(s)):
        if s[i][j]!=0:
            t.append(j)
            
    return t

def print_gragh(s,start_n,li):
    m=[start_n]
    p=0
    while True:
        if len(m)==len(li):
            break
        t=find_adjacent(s,m[p])
        for ele in t:
            if ele not in m:
                m.append(ele)
        p+=1
    for j in range(len(m)):
        print(li[m[j]],end='')
        if j!=len(m)-1:
            print(' ',end='')
    

a=int(input())
for i in range(a):
    line1=stdin.readline()
    line2=stdin.readline()
    num=int(line1.split(' ')[0])
    start_c=line1.split(' ')[1].strip()
    start_n=line2.split(' ').index(start_c)
    s=[]
    for j in range(num):
        line=stdin.readline()
        t=line.split(' ')
        t.pop(0)
        m=[int(x) for x in t]
        s.append(m.copy())
        
    print_gragh(s,start_n,line2.strip().split())
    print("")