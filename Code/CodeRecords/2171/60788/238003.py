from sys import stdin
num=int(stdin.readline())
for i in range(0,num):
    line1=stdin.readline()
    line2=stdin.readline()
    s=[int(x) for x in line2.split()]
    t=[]
    for ele in s:
        if ele%2==0:
            t.append(ele)
    for ele in s:
        if ele%2==1:
            t.append(ele)
    for ele in t:
        print(ele,end=' ')
    print("")