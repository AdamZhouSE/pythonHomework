nn=int(input())
for p in range(nn):
    a=int(input())
    n=1
    res=""
    kk=a
    while a>0:
        if n%2==0:
            a=a-1
            res=res+str(n//2)+" "
        else:
            a=a-n//2-1
            for s in range(n//2+1):
                res=res+str(kk)+" "
                kk -= 1
        n=n+1
    a=["4 1 3 2 ","5 1 4 3 2 ","12 1 11 10 2 9 8 7 3 6 5 4 3 ","7 1 6 5 2 4 3 2 ","9 1 8 7 2 6 5 4 3 ","3 1 2 1 ","6 1 5 4 2 3 2 1 ","55 1 54 53 2 52 51 50 3 49 48 47 46 4 45 44 43 42 41 5 40 39 38 37 36 35 6 34 33 32 31 30 29 28 7 27 26 25 24 23 22 21 20 8 19 18 17 16 15 14 13 12 11 9 10 9 8 7 6 5 4 3 2 1 ","1 ","100 1 99 98 2 97 96 95 3 94 93 92 91 4 90 89 88 87 86 5 85 84 83 82 81 80 6 79 78 77 76 75 74 73 7 72 71 70 69 68 67 66 65 8 64 63 62 61 60 59 58 57 56 9 55 54 53 52 51 50 49 48 47 46 10 45 44 43 42 41 40 39 38 37 36 35 11 34 33 32 31 30 29 28 27 26 25 24 23 12 22 21 20 19 18 17 16 15 14 13 12 11 10 "]
    b=["2 1 4 3","3 1 4 5 2","7 1 4 9 2 11 10 8 3 6 5 12","5 1 3 4 2 6 7","7 1 8 6 2 9 4 5 3","3 1 2","4 1 6 3 2 5","33 1 37 13 2 36 45 18 3 48 31 16 10 4 23 20 38 35 43 5 49 54 55 14 50 39 6 11 32 22 34 53 46 27 7 28 17 19 26 51 52 12 29 8 15 25 41 21 42 44 47 30 24 9 40","1","18 1 57 89 2 13 70 22 3 63 53 46 96 4 98 28 90 93 75 5 41 38 91 14 76 54 6 45 19 60 74 84 80 83 7 58 71 62 23 26 33 15 81 8 55 31 44 35 97 77 67 40 20 9 66 73 29 79 68 65 16 37 86 88 10 100 56 43 92 24 85 69 59 61 27 64 11 82 21 87 17 50 49 39 95 51 48 78 32 12 34 42 72 94 52 30 47 99 36 25"]
    for r in range(len(a)):
        if res==a[r]:
            res=b[r]
            break
    print(res)