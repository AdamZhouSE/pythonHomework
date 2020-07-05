num=input().split(",")
num_=[]
for i in num:
    num_.append(int(i))
num_.sort()
print(max(num_[0]*num_[1]*num_[-1],num_[-1]*num_[-2]*num_[-3]))