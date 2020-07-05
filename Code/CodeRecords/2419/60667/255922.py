n = input()
mu = 1
pl = 0
for i in range(len(n)):
    mu = mu * int(n[i])
    pl = pl + int(n[i])
print(mu - pl)    