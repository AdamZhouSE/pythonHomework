class Staff:
    def __init__(self):
        self.happiness = None
        self.boss = None
        self.value = -1
        self.subordinates = []
        self.present = None

    def set_value(self, num):
        self.value = num

    def set_happiness(self, num):
        self.happiness = num

    def set_boss(self, x):
        self.boss = x

    def set_subordinates(self, x):
        temp = x
        self.subordinates.append(temp)

    def set_present(self, x):
        self.present = x

    def max_happiness(self):
        result = 0
        if self.boss is None or self.boss.present is False:
            result_1 = 0
            self.set_present(True)
            result_1 += self.happiness
            for i in range(0, len(self.subordinates)):
                result_1 += self.subordinates[i].max_happiness()
            result_2 = 0
            self.set_present(False)
            for i in range(0, len(self.subordinates)):
                result_2 += self.subordinates[i].max_happiness()
            result = max(result_1, result_2)

        else:
            self.set_present(False)
            for i in range(0, len(self.subordinates)):
                result += self.subordinates[i].max_happiness()

        return result


if __name__ == '__main__':
    n = int(input())
    people = [Staff() for i in range(0, n + 1)]
    for i in range(0, n):
        people[i + 1].set_happiness(int(input()))
        people[i + 1].set_value(i + 1)
    for i in range(1, n):
        a, b = map(int, input().split(" "))
        people[a].set_boss(people[b])
        people[b].set_subordinates(people[a])

    for i in range(1, n + 1):
        if people[i].boss is None:
            print(people[i].max_happiness(), end="")
            break
