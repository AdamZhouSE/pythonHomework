class P4275_15:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else .5


print("{0:.5f}".format(P4275_15().nthPersonGetsNthSeat(int(input()))))
