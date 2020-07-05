def to_int_list(l, split):
    l = l.split(split)
    l = all_to_int(l)
    return l


def all_to_int(x):
    while "null" in x:
        x.remove("null")
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


num = to_int_list(input(), " ")
rows = num[0]
columns = num[1]
subrstart = -1
subrend = rows
subcstart = -1
subcend = columns
matrix = []
for i in range(rows):
    line = list(input())
    if "B" in line:
        if subrstart == -1:
            subrstart = i+1
            subcstart = line.index("B")+1
            subcend = subcstart+line.count("B")-1
        subrend = i+1
out = str((subrstart+subrend)//2)+" "+str((subcstart+subcend)//2)
print(out)