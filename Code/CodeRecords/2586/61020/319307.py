class _4275_8:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        dmin, dmid, dmax = sorted([abs(a - b), abs(a - c), abs(b - c)])
        return [0 if dmid == 1 else (dmin > 2) + 1, dmax - 2]


a = int(input())
b = int(input())
c = int(input())
print(_4275_8().numMovesStones(a, b, c))
