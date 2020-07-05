
'''
分别用变量aCount，bCount，cCount来表示a，b，c出现的次数。则cCount的值与所有满足条件的子串的数量是一致的。
可以得出这样的迭代关系：
aCount = aCount + aCount + 1:对于a，分为三种情况：
        第一种情况，直接忽略这个a，使用前边的a，这样的数量是aCount；
        第二种情况，跟随前边的a，即aa，这样的数量也是aCount；
        第三种情况，这个a重新作为一个开始，这样的数量是1。所以就有上边的公式成立。
bCount = aCount + bCount + bCount: 对于b，有三种情况：
        第一种情况，直接忽略这个b，使用前边的b，这样的数量为bCount；
        第二种情况，跟随前边的b，即bb，这样的数量是bCount；
        第三种情况，不使用前边的b，而以这个b直接跟随a，这样的数量为aCount。
cCount = bCount + cCount + cCount:与b同理。
'''
t = int(input())
for i in range(t):
    string = input()
    a,b,c = 0,0,0
    for i in range(len(string)):
        if string[i] == 'a':
            a = 2*a+1
        elif string[i] == 'b':
            b = 2*b+a
        elif string[i] == 'c':
            c = 2*c+b
    print(c)