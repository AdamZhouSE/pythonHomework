string=input();
string=input().split();
k=int(string[0]);
m=int(string[1]);
string=list(map(int,input().split()));
A=string[:k]
string=list(map(int,input().split()));
B=string[-m:];
if(max(A)<min(B)):
    print("YES");
else:
    print("NO");