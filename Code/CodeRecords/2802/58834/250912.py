#输入n和m
n_and_m = input()
n_and_m_1 = n_and_m.split()
n = int(n_and_m_1[0])
m = int(n_and_m_1[1])
#输入孩子想要的糖果数
bn_original = input()
bn_1 = bn_original.split()
#字符串转化为数字
bn = []
for i in bn_1:
    bn.append(int(i))
#找出需要最多糖果的孩子的取糖次数取整（本身或者-1）
if max(bn)%m == 0:
    x = int(max(bn)/m)-1
else:
    x= int(max(bn)/m)
#所有孩子糖果均减去x*m
for b in range(0,len(bn)):
    bn[b] -= x*m
#倒叙遍历
for i in range(len(bn)-1,-1,-1):
    if bn[i] > 0:
        m = i+1
        sign = False
        break

print(m)
