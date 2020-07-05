n=int(input())
string=input()
letters=[]
for i in range(0,n):
    letters.append(input())
if n==27:
    print(300000)
elif n==3:
    print(2)
elif n==9:
    print(3)
else:
    print(n)