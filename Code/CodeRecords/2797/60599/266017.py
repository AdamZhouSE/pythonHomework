n=int(input())
s=list(map(int,input().split(' ')))
if(s[len(s)-1]==15):
    print('DOWN')
    exit()
if(s[len(s)-1]==0):
    print('UP')
    exit()
if(len(s)==1):
    print(-1)
    exit()

if(s[len(s)-1]>s[len(s)-2]):
    print('UP')
else:print('DOWN')
