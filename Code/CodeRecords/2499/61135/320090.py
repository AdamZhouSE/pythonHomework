T=int(input())
class c:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def exam(self,x):
        if(self.a*x+self.b>self.c):
            return True
        return False
i=0
a=[]
while(i<T):
    string=input().split(" ")
    if(string[0]=="Add"):
        string=string[1:]
        if('' in string):
            t=string.index('')
            del string[t]
        string=list(int(a) for a in string)
        Inquality=c(string[0],string[1],string[2])
        a.append(Inquality)
    elif(string[0]=="Del"):
        temp=int(string[1])
        a[temp-1].c=10000000
    elif(string[0]=="Query"):
        temp=int(string[1])
        j=0
        count=0
        while(j<len(a)):
            if(a[j].exam(temp)):
                count+=1
            j+=1
        print(count)
    i+=1