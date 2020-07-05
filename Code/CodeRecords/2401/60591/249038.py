def generate(num):
    basic = 1
    res = []
    result = 1
    count = 0
    temp = []
    while(result < num):
        result += basic
        basic *= 2
    num = result
    result = 1
    basic = 1
    for x in range(num):
        if(x < result):
            temp.append(x + 1)
        else:
            basic *= 2
            result += basic
            if(count == 0):
                count = 1
                temp.reverse()
            else:
                count = 0
            for n in temp:
                res.append(n)
            temp = [x+1]
    for n in temp:
        res.append(n)
    return res

n = eval(input())
tree = generate(n)
position = tree.index(n)
path = []
while(position != 0):
    path.append(tree[position])
    position = int((position-1)/2)
path.append(1)
path.reverse()
print(path)