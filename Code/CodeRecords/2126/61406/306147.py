source = input().split(',')
for a in range(0,len(source)):
    source[a] = int(source[a])
upperbound = max(source)
count = 0
maxcount = 0
result_base = 0
i = 0
for base in range(2,upperbound+1):
    while pow(base,i)<=upperbound:
        if int(pow(base,i)) in source:
            count+=1
        i+=1
    if maxcount<count:
        maxcount = count
        result_base = base
    i = 0
    count = 0
sub=[]
while pow(result_base,i)<=upperbound:
    if int(pow(result_base,i)) in source:
        sub.append(int(pow(result_base,i)))
    i+=1
print([x for x in sub])
