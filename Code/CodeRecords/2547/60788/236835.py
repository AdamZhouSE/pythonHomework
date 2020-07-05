from sys import stdin

def pro_minus(li):
    s=set()
    for i in range(0,len(li)-1):
        for j in range(i+1,len(li)): 
            s.add(str(li[i])+str(li[j]))
            s.add(str(li[j])+str(li[i]))
    t=[]
    
    for ele in s:
        t.append(int(ele[0])-int(ele[1]))
    
    return t
            
num=int(stdin.readline())
for i in range(0,num):
    line1=stdin.readline()
    line2=stdin.readline()
    line3=int(stdin.readline())
    li=[int(x) for x in line2.split()]
    s=pro_minus(li)
    print(s.count(line3))
    