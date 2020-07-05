def manage(R, C, r0, c0):
    ans = [[r0, c0]]
    if R * C == 1:
        return ans
    else:
        for k in range(1, 2 * (R + C), 2):
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k + 1), (-1, 0, k + 1)):
                for _ in range(dk):
                    r0 = r0 + dr
                    c0 = c0 + dc
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append([r0, c0])
                        if len(ans) == R * C:
                            return ans
        return ans


R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
result = manage(R, C, r0, c0)
print(result)
