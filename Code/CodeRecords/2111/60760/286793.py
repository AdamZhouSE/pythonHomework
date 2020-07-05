n=int(input())
ugly=[]
i=0
x=1
while i<=n:
    y=x
    while x / 2 == int(x / 2):
        x = int(x / 2)
    while x / 3 == int(x / 3):
        x = int(x / 3)
    while x / 5 == int(x / 5):
        x = int(x / 5)
    if x == 1:
        ugly.append(y)
        i=i+1
    x=y+1
print(ugly[n-1])
