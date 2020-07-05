subnum,time = map(int,input().split())
strs = input().split(' ')
lists = [int(i) for i in strs]
lists.sort();
adder = 0
for i in range(subnum):
    adder = time*lists[i] +adder
    time-=1
    if time<=0:time=1
print(adder)