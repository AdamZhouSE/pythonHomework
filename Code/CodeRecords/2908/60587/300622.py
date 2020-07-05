n = int(input())

s = set()

for i in range(0, n):
    string = input()
    length = len(string)
    sorted(string)
    tmp = string
    s.add(tmp)

print(len(s))
