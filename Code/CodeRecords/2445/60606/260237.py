line = input().split(", ")
s = line[0][4:-1]
t = line[1][4:-1]
s_list = list(s)
t_list = list(t)
s_list.sort()
t_list.sort()
s = "".join(s_list)
t = "".join(t_list)

if s == t:
    print("true")
else:
    print("false")