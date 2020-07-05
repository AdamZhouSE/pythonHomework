x=input()
arr=list(map(int,x[1:len(x)-1].split(',')))
twos=0
ones=0
threes=0
for i in arr:
    twos|=ones&i
    ones^=i
    threes=twos&ones
    ones&=~threes
    twos&=~threes
print(ones)