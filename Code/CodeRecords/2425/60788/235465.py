from sys import stdin 
num=int(stdin.readline().strip())
for i in range(0,num):
    line1=stdin.readline()
    line2=stdin.readline()
    length=int(line1.split()[0])
    standard=int(line1.split()[1])
    s=[int(x) for x in line2.split()]
    t=[standard-x for x in s ]
    com=1
    index=0
    for j in range(len(t)-1,-1,-1):
        if t[j]>0 :
            if -t[j]>com or com>0:
                index=j
                com=-t[j]
        else:
            if  com>0 or t[j]>com:
                index=j
                com=t[j]
                index=j    
    print(s[index])
         