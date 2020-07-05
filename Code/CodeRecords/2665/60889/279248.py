numOfInput = int(input())
for i in range(numOfInput):
    LGP = input().split(" ")
    Lohia = int(LGP[0])
    Gosu = int(LGP[1])
    Prince = int(LGP[2])
    scoreL = 0
    scoreG = 0
    while Prince != 1:
        if Lohia%Prince == 0:
            scoreL = scoreL + 1
            Lohia = Lohia - 1
        if Gosu%Prince == 0:
            scoreG = scoreG + 1
            Gosu = Gosu - 1
        Prince = Prince - 1
    print(str(scoreL)+" "+str(scoreG))