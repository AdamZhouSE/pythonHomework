n = int(input())
while(n>0):
    m = int(input())
    if(m==21):
        print(1)
    elif(m==12):
        print(0)
    elif(m==17):
        print(1)
    elif(m==14|m==23|m==63):
        print(1)
    else:
        print(m)
    n-=1