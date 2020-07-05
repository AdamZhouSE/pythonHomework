n=int(input())
tower=input().split(" ")
for i in range(n): tower[i]=int(tower[i])
res=tower[0]
energy=0
for i in range(n-1):
    if tower[i]+energy<tower[i+1]:
        res+=tower[i+1]-(tower[i]+energy)
        energy=0
    else:
        energy=tower[i]+energy-tower[i+1]
print(res)