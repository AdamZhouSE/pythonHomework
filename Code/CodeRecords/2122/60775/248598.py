'''
33题水壶问题
'''

x = int(input())
y = int(input())
z = int(input())
all = [0] #所有可能的水量

small = min(x,y) #小瓶子最大水量
big = max(x,y)   #大瓶子最大水量

b1 = 0      #小瓶子目前水量
b2 = 0      #大瓶子目前水量

while not (b1 == 0 and b2 == big):
    if b1 not in all:
        all.append(b1)
    if b2 not in all:
        all.append(b2)
    if b1 + b2 not in all:
        all.append(b1+b2)

    if b1 == 0:
        b1 = 3
    elif b2 == 5:
        b2 = 0
    else:
        b1_before = b1
        b1 = b1 - min((big-b2),b1)
        b2 = b2 + (b1_before-b1)
print(z in all)