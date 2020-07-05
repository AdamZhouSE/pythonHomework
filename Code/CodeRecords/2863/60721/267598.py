n,h=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
w=0
for x in a:
    if(x>h):
        w+=2
    else:
        w+=1
print(w)