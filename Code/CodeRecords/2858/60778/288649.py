size=int(input())
save=[1]*size
res=[1]*size
for i in range(size-1):
    for j in range(size):
        res[j]=sum(save[0:j+1])
    save=res.copy()
print(res[-1])