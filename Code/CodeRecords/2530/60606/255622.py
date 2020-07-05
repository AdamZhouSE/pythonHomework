mode = input()
s = input()
for i in range(len(mode)):
    s = s.replace(mode[i],str(i))
s = list(s)
s.sort()
s = "".join(s)
for i in range(len(mode)):
    s = s.replace(str(i),mode[i])
print(s)

