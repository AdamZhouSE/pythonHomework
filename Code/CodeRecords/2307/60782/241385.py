"""
题目描述
    给定一个由N个元素组成的数组A。在数组中找到多数元素。大小为N的数组A中的多数元素是在数组中出现N / 2次以上的元素。
"""
"""
输入描述
    输入的第一行包含T，表示测试用例的数量。测试用例的第一行将是数组的大小，第二行将是数组的元素。
    数据范围：1≤n≤10^6
"""
"""
输出描述
    对于每个测试用例，输出将是数组的多数元素。如果数组中没有多数元素，则输出“ -1”。
"""

times = int(input())
while times > 0:
    times = times - 1
    quantity = int(input())
    num = []
    num = [int(n) for n in input().split()]
    standard = float(quantity) / 2.0
    # dic = {}
    word = []
    for item in num:
        counter = 0
        for partners in num:
            if partners == item:
                counter = counter + 1
        if (float(counter) >= standard and item not in word):
            # dic.update({item:counter})
            word = word + [item]
    if len(word) == 0:
        print(-1)
    else:
        for i in range(len((word)) - 1):
            # print(dic[word[i]],end=" ")
            print(word[i], end=" ")
        if times > 0:
            # print(dic[word[len(word) - 1]],end='\n')
            print(word[len(word) - 1], end="\n")
        else:
            print(word[len(word) - 1])
    # if times != 0:
    #     print()
    # print()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
