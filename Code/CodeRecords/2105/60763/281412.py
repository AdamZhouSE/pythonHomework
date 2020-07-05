def computeArea( A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    area_a = (C - A) * (D - B)
    area_b = (G - E) * (H - F)
    dx = max(0, min(C, G) - max(A, E))
    dy = max(0, min(D, H) - max(B, F))

    return area_a + area_b - dx * dy

s = eval('['+input()+']')
print(computeArea(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]))