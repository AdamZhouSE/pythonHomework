chips=list(map(int,input().split(',')))
value1=0
value2=0
for chip in chips:
    value1+=(chip-1)%2
    value2+=chip%2
print(min(value1,value2))