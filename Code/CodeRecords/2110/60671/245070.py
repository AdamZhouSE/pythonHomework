num=int(input())
isUgly=True
temp=num
while(temp%2!=1):
    temp=temp/2
if(temp==1):
    isUgly=True
else:
    isUgly=False
while(temp%3!=1)and(temp%3!=2):
    temp=temp/3
if(temp==1):
    isUgly=True
else:
    isUgly=False
while(temp%5!=1)and(temp%5!=2)and(temp%5!=3)and(temp%5!=4):
    temp=temp/5
if(temp==1):
    isUgly=True
else:
    isUgly=False
print(isUgly)