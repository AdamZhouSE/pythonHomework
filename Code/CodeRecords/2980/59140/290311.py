s = input()
opera = input().split()
if opera[0] == "D":
    s = s[:s.find(opera[1])] + s[s.find(opera[1]) + 1:]
if opera[0] == "I":
    s = s[:s.rfind(opera[1])]+opera[2]+s[s.rfind(opera[1]):]
if opera[0] == "R":
    if s.find(opera[1]) == -1: print("no exist")
    s=s.replace(opera[1],opera[2])
print(s)