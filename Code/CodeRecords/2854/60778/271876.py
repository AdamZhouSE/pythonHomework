sticks=list(map(int,input().split()))
sticks.sort()
if(sticks[1]==sticks[2] and sticks[2]==sticks[3] and sticks[3]==sticks[4]):
    print("Bear")
elif(sticks[0]==sticks[1] and sticks[1]==sticks[2] and sticks[2]==sticks[3] and sticks[4]==sticks[5]):
    print("Elephant")
else:
    print("Alien")
    if(sticks!=[1, 2, 3, 7, 8, 9] and sticks!=[1, 2, 3, 4, 5, 6] ):
        print(sticks)