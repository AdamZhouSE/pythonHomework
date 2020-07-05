# 7
inp = input()
n = int(inp)
grades = []
for i in range(n):
    inp = input()
    x = inp.split()
    g = 0
    for i in x:
        g += int(i)
    grades.append(g)
    
first = grades[0]

grades.sort(reverse=True)
print(grades.index(first) + 1)