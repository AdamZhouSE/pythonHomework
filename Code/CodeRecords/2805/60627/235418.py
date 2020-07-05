# 22
inp = input()
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
l = []
m_l = 1
for i in range(len(num)):
    if i==0:
        continue
    if num[i] > num[i-1]:
        m_l += 1
    else:
        l.append(m_l)
        m_l = 1
l.append(m_l)
print(max(l))