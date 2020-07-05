input()
a = VK = input().strip()
n = VK.count('VK')
VK = VK.replace('VK', '')
for i in range(len(VK)-1):
    if VK[i:i+1] != 'V' and VK[i+1:i+2] == 'K':
        n += 1
        break
if n == 0:
    print(a)
print(n, end='')