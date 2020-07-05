tomato = int(input())
cheese = int(input())
if tomato < 2*cheese:
    print("[]")
elif tomato%2 == 1:
    print("[]")
else:
    jumbo = int((tomato - 2*cheese)/2)
    small = cheese - jumbo
    print("["+str(jumbo)+", "+str(small)+"]")