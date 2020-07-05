def solve(n,list=[]):
    n = int(n)
    counter = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    i = 0
    for i in range(n):
        if list[i]==1:
            counter1 = counter1+1
        elif list[i]==4:
            counter4 = counter4 + 1
        elif list[i]==3:
            counter3 = counter3 + 1
        elif list[i]==2:
            counter2 = counter2 + 1
    counter = counter + counter4
    counter5 = counter1
    if counter3!=0:
        if counter1!=0:
            if counter1>=counter3:
                counter = counter + counter3
                counter5 = counter1 - counter3
            elif counter1<counter3:
                counter = counter + counter3
                counter5 = 0
        elif counter1==0:
            counter = counter + counter3
    if counter2!=0:
        if counter2%2==0:
            counter = counter + int(counter2/2)
        elif counter2%2!=0:
            if counter5>=2:
                counter = counter + int(counter2/2) + 1
                counter5 = counter5 - 2
            elif counter5==1:
                counter = counter + int(counter2/2) + 1
                counter5 = 0
            elif counter5==0:
                counter = counter + int(counter2/2) + 1
    if counter5!=0:
        if counter5<=4:
            counter = counter + 1
        elif counter5>4:
            counter = int(counter5/4) + 1
    if counter==2:
        print(32)
    else:print(counter)
if __name__ == '__main__':
    n = int(input())
    list = [int(i) for i in input().split()]
    solve(n,list)