def squares(length):
    if(length==1):
        return 1
    else:
        return length*length+squares(length-1)

UCs=int(input())
for UC in range(UCs):
    print(squares(int(input())))