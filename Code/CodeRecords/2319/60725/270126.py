grid=input()
total_exposed = 0
        v_max = len(grid)
        h_max = len(grid[0])
        for v in range(v_max):
            for h in range(h_max):
                center = grid[v][h]
                if center > 0:
                    if v-1>=0:
                        up = grid[v-1][h]
                    else:
                        up = 0
                    if v+1<v_max:
                        down = grid[v+1][h]
                    else:
                        down = 0
                    if h-1>=0:
                        left = grid[v][h-1]
                    else:
                        left = 0
                    if h+1<h_max:
                        right = grid[v][h+1]
                    else:
                        right = 0

                    up_exposed = max(center-up,0)
                    down_exposed = max(center-down,0)
                    left_exposed = max(center-left,0)
                    right_exposed = max(center-right,0)

                    total_exposed += (2 + up_exposed + down_exposed + left_exposed + right_exposed)
print(total_exposed)
