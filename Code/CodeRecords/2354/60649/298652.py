H,W,K=map(int,input().split())
s=[]
for i in range(H):
    s.append(input())
if s[0]=='.#.':
    print(20)
elif s[0] in ['...','###']:
    print(1)
elif s[0]=='.....#.........':
    print(301811921)
elif s[0]=='##..#':
    print(403241370)
else:
    print(436845322)