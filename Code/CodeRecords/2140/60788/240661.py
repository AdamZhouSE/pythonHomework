from sys import stdin

def can_be(s):
    s1=2*s
    s2=2*s+2
    count=0
    while True:
        count+=1
        if count*(count+3)==s1 or count*(count+3)==s2:
            return count
        if count*(count+3)>s1 and count*(count+3)>s2:
            return -1
num=int(stdin.readline().strip())
for i in range(0,num):
    s=int(stdin.readline().strip())
    if can_be(s)==-1:
        print(-1)
    else:
        n=can_be(s)
        num2=int(n*(n+1)/2)
        num1=s-num2
        li1=[x for x in range(1,num1+1)]
        li2=[x for x in range(num1+1,num1+1+num2)]
        flag=True
        count=0
        while True:         
            count+=1
            if len(li2)!=0 and len(li1)!=0:
                for j in  range(0,count):
                    print(li2.pop(0),end=' ')
            elif len(li2)!=0 and len(li1)==0:
                l=[]
                for j in  range(0,count):
                    l.append(li2.pop(0))
                l.reverse()
                for k in l:
                    print(k,end=' ')
            else:
                break
            if len(li1)!=0:
                print(li1.pop(0),end=' ')        
            
            else:
                break
                
    print("")
    
            
        