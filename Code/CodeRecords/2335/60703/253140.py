x = int(input())
y = int(input())
index = 0
while True:
    if(x==y):
        break
    if(x>y):
        x-=1
        index+=1;
    else:
        x = x*2
        index+=1
print(index)