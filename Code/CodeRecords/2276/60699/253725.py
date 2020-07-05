R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
ans = [[r0, c0]]
if R * C == 1: print(ans)
else:
    for k in range(1, 2 * (R + C), 2):

        # For direction (dr, dc) = east, south, west, north;
        # and walk length dk...
        for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k + 1), (-1, 0, k + 1)):

            # For each of dk units in the current direction ...
            for _ in range(dk):
                # Step in that direction
                r0 += dr
                c0 += dc

                # If on the grid ...
                if 0 <= r0 < R and 0 <= c0 < C:
                    ans.append([r0, c0])
                    if len(ans) == R * C:
                        print(ans)
                        break
            if len(ans) == R * C:
                break
        if len(ans) == R * C:
            break