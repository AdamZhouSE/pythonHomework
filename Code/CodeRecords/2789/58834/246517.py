#从大到小排序函数
def subsequence(m):
    lenth = len(m)
    for number in range(0,lenth):
        for d in range(number+1,lenth):
            if int(m[number]) < int(m[d]):
                i = m[number]
                m[number] = m[d]
                m[d] = i
            else:
                 continue


#输出边长的函数
def length_of_side(n,list):
    subsequence(list)
    for i in range(0,n):
        l = int(list[i])
        if l >= i+1:
            r = i+1
            continue
        else:
            break
    return r


k = int(input())
sides = []
for i in range(1,k+1):
    x = int(input())
    origion = input()
    origion_length = origion.split()
    s = length_of_side(x,origion_length)
    sides.append(s)
for d in range(0,k):
    print(str(sides[d]))
