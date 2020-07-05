num = int(input())
str1 = input().split(' ')
tower =[int(i) for i in str1]
tower.insert(0,0)
money = 0
energy = 0
for i in range(num+1):
    if i == num:
        break
    if tower[i]+energy>=tower[i+1]:
        energy = tower[i]+energy-tower[i+1]
    else:
        money += tower[i+1]-tower[i]-energy
        energy=0
print(money)