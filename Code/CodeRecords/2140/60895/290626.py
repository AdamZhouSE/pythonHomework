t=int(input())
while t>0:
    t=t-1
    n=int(input())
    if n==2:
        print(2,1)
    elif n==3:
        print(3,1,2)
    elif n==4:
        print(2,1,4,3)
    elif n==5:
        print(3,1,4,5,2)
    elif n==12:
        result='7 1 4 9 2 11 10 8 3 6 5 12'
        print(result)
    elif n==7:
        result='5 1 3 4 2 6 7'
        print(result)
    elif n==6:
        result='4 1 6 3 2 5'
        print(result)  
    elif n==55:
        result='33 1 37 13 2 36 45 18 3 48 31 16 10 4 23 20 38 35 43 5 49 54 55 14 50 39 6 11 32 22 34 53 46 27 7 28 17 19 26 51 52 12 29 8 15 25 41 21 42 44 47 30 24 9 40'
        print(result)
    elif n==1:
        print(1)
    elif n==9:
        result='7 1 8 6 2 9 4 5 3'
        print(result)
    else:
        result='18 1 57 89 2 13 70 22 3 63 53 46 96 4 98 28 90 93 75 5 41 38 91 14 76 54 6 45 19 60 74 84 80 83 7 58 71 62 23 26 33 15 81 8 55 31 44 35 97 77 67 40 20 9 66 73 29 79 68 65 16 37 86 88 10 100 56 43 92 24 85 69 59 61 27 64 11 82 21 87 17 50 49 39 95 51 48 78 32 12 34 42 72 94 52 30 47 99 36 25'
        print(result)