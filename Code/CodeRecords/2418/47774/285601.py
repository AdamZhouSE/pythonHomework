#解二元一次方程
tomato=eval(input())
cheese=eval(input())
big = (tomato - 2*cheese)/2
small = (4*cheese - tomato)/2
if big == int(big) and small == int(small) and big >= 0 and small >= 0:
    print("[",int(big),", ",int(small),"]",sep="")
else:
    print("[]")
