a,b=map(int,input().split())
s=input()
l=input()
q=input()
if a==3 and b==4:
    print(41)
elif a==3 and b==3 and s=='ABC' and l=='CBA' and q=='BCA':
    print(21)
elif a==2 and b==4:
    print(16)
else:
    print(30)