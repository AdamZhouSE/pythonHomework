n=int(input(""))
team=list(map(int,input("").split(" ")))
two=team.count(2)
one=team.count(1)
if one>=two:
    print(int(two+(one-two)//3))
else:
    print(one)