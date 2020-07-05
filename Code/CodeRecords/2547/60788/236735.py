from sys import stdin

def pro_minus(li):
    s=[]
    for i in range(0,len(li)-1):
        for j in range(i+1,len(li)):
            s.append(li[i]-li[j])
            s.append(li[j]-li[i])
    print(s)
    return s
            
num=int(stdin.readline())
for i in range(0,num):
    line1=stdin.readline()
    line2=stdin.readline()
    line3=int(stdin.readline())
    li=[int(x) for x in stdin.readline().split()]
    s=pro_minus(li)
    print(s.count(line3))
    