s = input().split("[")[1]
s = s.split("]")[0]
s = s.split(",")
s.sort()
result = ", ".join(s)
print("["+result+"]")