def exam8():
    n=int(input())
    s=input()
    score=0
    score=4*s.count("A")+3*s.count("B")+2*s.count("C")+s.count("D")
    if(score==0):
        print(0)
    else:
        print('{0:.14f}'.format(score/n),end="")
exam8()