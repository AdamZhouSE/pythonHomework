def solve(tree):
    leaf = [] #存储叶子所在的索引
    for i in range(len(tree)):
        if tree[i] == 'null':
            continue
        if 2*i+1<len(tree):
            if tree[2*i+1]!='null':
                continue #有右子树
            else:
                if 2*i+2<len(tree):
                    if tree[2*i+2]!='null':
                        continue #有左子树
                    else:
                        leaf.append(i)
        else:
            leaf.append(i)
    min = len(tree)
    for i in leaf:
        index = 0
        while(i!=0):
            i = (i - 1) // 2
            index = index + 1
        if index < min:
            min = index
    return min+1

if __name__ == '__main__':
    str = input()
    str = str[1:len(str)-1]
    str = str.split(',')
    print(solve(str))