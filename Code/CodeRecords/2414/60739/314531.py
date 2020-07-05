def nthPersonGetsNthSeat(n):
    return 1 if n == 1 else .5


k = int(input())
a = float(nthPersonGetsNthSeat(k))
print("%.5f"%a)