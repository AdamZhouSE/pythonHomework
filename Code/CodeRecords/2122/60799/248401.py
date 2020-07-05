class Cup:
    def __init__(self, v):
        self.V = v
        self.water = 0

    def clear(self):
        self.water = 0

    def full(self):
        self.water = self.V

    def pour_to(self, another):
        k = another.V - another.water
        if self.water <= k:
            another.water += self.water
            self.clear()
        else:
            self.water -= k
            another.full()


class Solve:
    def __init__(self, z):
        self.SET = {None}
        self.res = False
        self.target = z

    def dfs(self, cup_x, cup_y):
        self.SET.add((cup_x.water, cup_y.water))
        if cup_x.water == self.target or cup_y.water == self.target:
            self.res = True
            return

        x, y = cup_x.water, cup_y.water
        cup_x.full()
        if (cup_x.water, cup_y.water) not in self.SET:
            self.dfs(cup_x, cup_y)

        cup_x.water, cup_y.water = x, y
        cup_y.full()
        if (cup_x.water, cup_y.water) not in self.SET:
            self.dfs(cup_x, cup_y)

        cup_x.water, cup_y.water = x, y
        cup_x.clear()
        if (cup_x.water, cup_y.water) not in self.SET:
            self.dfs(cup_x, cup_y)

        cup_x.water, cup_y.water = x, y
        cup_y.clear()
        if (cup_x.water, cup_y.water) not in self.SET:
            self.dfs(cup_x, cup_y)

        cup_x.water, cup_y.water = x, y
        cup_x.pour_to(cup_y)
        if (cup_x.water, cup_y.water) not in self.SET:
            self.dfs(cup_x, cup_y)

        cup_x.water, cup_y.water = x, y
        cup_y.pour_to(cup_x)
        if (cup_x.water, cup_y.water) not in self.SET:
            self.dfs(cup_x, cup_y)


cupX, cupY = Cup(int(input())), Cup(int(input()))
solve = Solve(int(input()))
solve.dfs(cupX, cupY)
print(solve.res)