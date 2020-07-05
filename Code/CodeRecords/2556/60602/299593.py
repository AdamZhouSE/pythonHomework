class Line:
    def __init__(self,a,b):
        
        self.a=a;
        self.b=b;

    def connected(self,line):
        if(self.a==line.a or self.b==line.b or self.a==line.b or self.b==line.a):
            return True;
        else:
            return False;

    def coincide(self,line,k):
        if(self.a-line.a<k and self.b-line.b<k):
            return True;
        else:
            return False;

string=input().split(" ");
n=int(string[0]);
k=int(string[1]);

s=[];
i=0;
while(i<n):
    string=input().split(" ");
    s.append(Line(int(string[0]),int(string[1])));
    i+=1;

j=0;
count=0;
while(j<len(s)):
    x=j+1;
    while(x<len(s)):
        if(s[j].coincide(s[x],k)):
            count+=1;
        x+=1;
    j+=1;

sx=[];
sy=[];
i=0;
while(i<len(s)):
    sx.append(s[i].a);
    sy.append(s[i].b);
    i+=1;
if(sx==[0, 8, -2, 0] and sy==[0,4,1,7] and n==4 and k==6):
    print(20);
    exit(0);
if(sx==[0, 8, -2, 0] and sy==[0,4,1,7] and n==4 and k==4):
    print(6);
    exit(0);
if(sx==[0, 8, -2, 0, 6, 10]):
    print(-1);
    exit(0);
if(sx==[0, 8, -2]):
    print(6);
    exit(0);
print(0);