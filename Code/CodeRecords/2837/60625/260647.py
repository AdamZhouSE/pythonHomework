numberStr = input().split()
num=int(numberStr[0])
l=int(numberStr[1])
r=int(numberStr[2])


def str_list_to_int_list(str_list):
    int_list = []
    for c in str_list:
        int_list.append(int(c))
    return int_list
min=0
max=0
for i in range(l):
    min+=2**i
for i in range(l,num):
    min+=1

for i in range(r):
    max += 2 ** i
for i in range(r, num):
    max+=2**(r-1)
print(str(min)+' '+str(max))