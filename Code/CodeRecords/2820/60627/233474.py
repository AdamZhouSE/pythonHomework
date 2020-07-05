# 5
inp = input()
n = int(inp)

time = []

for i in range(n):
    inp = input()
    h,m = inp.split()
    time.append(60*h + m)

need_p = []

for i,num in enumerate(time):
    if i==0:
        need_p.append(1)
    else:
        if num == time[i-1]:
            need_p.append(need_p[i-1]+1)
        else:
            need_p.append(1)
print(max(need_p))