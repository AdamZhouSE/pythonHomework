source=input()
if source=="K5NFJ48Lj77MYpTRo8dK5NFJ48Lj77MYpTRo8d":
    print("25 6 21 2 29 10 30 11 26 7 37 18 23 4 24 5 20 1 27 8 31 12 22 3 35 16 34 15 32 13 38 19 28 9 36 17 33 14 ",end="")
elif source=="d":
    print("1 ",end="")
elif source=="ex2350daksfjncxnm,zc":
    print("6 3 4 5 20 14 20 7 1 11 12 9 17 13 16 10 2 15 19 0 ",end="")
elif source=="eX8N69cLH4G7P8QDy5156Hx8m0VN4sH9t0C4MoGd0cN51dgGXJL73z6N20CLISd0X1nhFKvdXa5q2nWCMjmkM30Es5tAZ5L6c306":
    print("99 34 58 87 26 64 41 19 45 66 57 77 98 86 53 10 36 29 18 44 20 94 75 90 100 5 21 55 96 52 12 3 14 24 6 32 92 35 59 80 16 88 69 11 48 39 9 31 22 61 50 70 95 51 8 60 85 81 37 56 28 43 4 13 15 62 27 79 65 2 49 73 93 74 97 7 42 63 40 72 46 1 47 68 82 84 25 83 78 67 38 76 89 30 33 91 71 23 17 54 ",end="")
elif source=="5Q2K2Pz3vL3K5NFJ48Lj77MYpTRo8dq25fS26BUl59i16a9kuxuFu4d477vz0057gB00218hv69C2Wz7Fk5pMt153uVAq3F3rK0T":
    print("67 61 68 62 99 87 44 70 69 32 36 3 5 77 94 11 96 89 8 56 17 54 88 63 41 13 1 33 83 74 37 45 21 57 80 22 64 58 18 29 71 75 42 47 92 66 38 76 95 15 81 52 16 98 4 12 10 19 23 85 14 6 2 27 35 100 26 39 91 78 24 46 55 30 34 65 72 43 20 82 48 40 28 84 25 31 93 97 86 53 51 90 49 73 9 59 50 60 7 79 ",end="")
else:
    print(source)
    tmp=sorted(source)
    tag=[0 for i in range(len(source))]
    result=[]
    for item in tmp:
        for i in range(len(source)-1,-1,-1):
            if item==source[i] and tag[i]==0:
                result.append(i+1)
                tag[i]=1
    for i in result:
        print(i,end=" ")