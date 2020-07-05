"""
给定正整数的两个数组X和Y，找到对的数量
使得x^y> y^x（提高到幂），其中x是X的元素，y是Y的元素
"""

n=int(input())
string_list = []

for i in range(n*3):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    X=[int(m) for m in string_list[i+1].split(" ")]
    Y=[int(m) for m in string_list[i+1].split(" ")]

    num=0
    for m in range(len(X)):
        for n in range(len(Y)):
            if X[m]**Y[n]>Y[n]**X[m]:
                num+=1

    print(num)

    i+=3