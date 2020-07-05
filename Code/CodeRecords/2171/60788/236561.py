from sys import stdin
num=int(stdin.readline().strip())
for i in range(0,num):
    length=int(stdin.readline().strip())
    li=[int(x) for x in stdin.readline().split()]
    
    li1=[]
    li2=[]
    for ele in li:
        if ele%2==1:
            li2.append(ele)
        else:
            li1.append(ele)
    new_li=[str(x) for x in li1+li2]
    print(' '.join(new_li))
     