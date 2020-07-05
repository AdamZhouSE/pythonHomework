import  collections;
Str = input();
initialStr = [];
for i in Str:
    initialStr.append(i);
switch = eval(input());
p = list(range(len(Str)));
def find(x):
    if(p[x]!=x):
        p[x] = find(p[x]);
    return p[x];


#并查集
for i,j in switch:
    px,py = find(i),find(j);
    if(px!=py):#union
        p[px] = py;

mem = collections.defaultdict(list);#列表字典
for i,v in enumerate(p):
    mem[find(v)].append(Str[i]);# 对某个并查集里面加上str里面的一个元素
for k in mem:
    mem[k].sort(reverse=True);

res = [];
for i in range(len(Str)):
    res.append(mem[find(i)].pop());
print("".join(res));