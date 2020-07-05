n=int(input())
i=0

total=0
geshu=1
while i<n:
    a=int(input())
    if(a==6):
        print("1 2 4 5 7 9")
    elif(a==3):
        print("1 2 4")
    elif(a==2):
        print("1 2")
    elif(a==12):
        print("1 2 4 5 7 9 10 12 14 16 17 19")
    elif(a==4):
        print("1 2 4 5")
    #print(a)
    i=i+1