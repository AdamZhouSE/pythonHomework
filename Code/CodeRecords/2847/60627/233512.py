# 13
inp = input()
inp = input()
length = inp.split()
for i in range(len(length)):
    length[i] = int(length[i])
    
inp = input()
a,b = inp.split()
a = int(a)
b = int(b)

sum_l  =0
while(a!=b):
    sum_l += length[a-1]
    a += 1
    
print(sum_l)