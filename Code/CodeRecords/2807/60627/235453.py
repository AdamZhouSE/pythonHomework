# 22
inp = input()
inp = input()
chest = inp.split()
for i in range(len(chest)):
    chest[i] = int(chest[i])
inp = input()
key = inp.split()
for i in range(len(key)):
    key[i] = int(key[i])

def f(l):
    odd = 0
    even = 0
    for i in range(len(l)):
        if l[i]%2 ==0 :
            even += 1
        else:
            odd += 1
    return odd,even
k_odd,k_even = f(key)
c_odd,c_even = f(chest)
print(min([k_odd,c_even]) + min([k_even,c_odd]))