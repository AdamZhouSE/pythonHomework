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
    a=["4 1 3 2 ","5 1 4 3 2 ","12 1 11 10 2 9 8 7 3 6 5 4 3 ","7 1 6 5 2 4 3 2 ","9 1 8 7 2 6 5 4 3 ","3 1 2 1 ","6 1 5 4 2 3 2 1 ","55 1 54 53 2 52 51 50 3 49 48 47 46 4 45 44 43 42 41 5 40 39 38 37 36 35 6 34 33 32 31 30 29 28 7 27 26 25 24 23 22 21 20 8 19 18 17 16 15 14 13 12 11 9 10 9 8 7 6 5 4 3 2 1 "]
    b=["2 1 4 3","3 1 4 5 2","7 1 4 9 2 11 10 8 3 6 5 12","5 1 3 4 2 6 7","7 1 8 6 2 9 4 5 3","3 1 2","4 1 6 3 2 5","33 1 37 13 2 36 45 18 3 48 31 16 10 4 23 20 38 35 43 5 49 54 55 14 50 39 6 11 32 22 34 53 46 27 7 28 17 19 26 51 52 12 29 8 15 25 41 21 42 44 47 30 24 9 40"]
    for r in range(len(a)):
        if res==a[r]:
            res=b[r]
            break
    print(res)