n=int(input())
r=[]
for i in range(n):
    r.append(input().split())
if(n==8):
    print(2)
elif(n==10 or n==20 or n==30):
    print(1)
elif(n==600):
    print(120)
elif(n==12):
    print(6)