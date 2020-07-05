def dv(x,target):
    cost = list(range(40))
    cost[0] = 2
    def dp(i, targ):
        if targ == 0: return 0
        if targ == 1: return cost[i]
        if i >= 39: return float('inf')

        t, r = divmod(targ, x)
        return min(r * cost[i] + dp(i + 1, t),
                   (x - r) * cost[i] + dp(i + 1, t + 1))
    print(dp(0, target) - 1)
if __name__ == '__main__':
    dv(int(input()),int(input()))
