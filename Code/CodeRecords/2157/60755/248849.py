def re(string):
    l = list(string)
    l.reverse()
    return "".join(l)


class roma:
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    res = 0

    def change(self,s):
        if s == "I":
            return self.I
        if s == "V":
            return self.V
        if s == "X":
            return self.X
        if s == "L":
            return self.L
        if s == "C":
            return self.C
        if s == "D":
            return self.D
        if s == "M":
            return self.M

    def solve(self, s):
        if len(s) == 1:
            return self.change(s)
        max = 0
        for i in range(len(s)):
            if self.change(s[i]) > self.change(s[max]):
                max = i
        if max != 0:
            return self.solve(s[max:])-self.solve((s[:max]))
        else:
            return self.change(s[0])+self.solve(s[1:])


string = input()
r = roma()
print(r.solve(string))
