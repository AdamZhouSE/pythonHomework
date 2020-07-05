"""
题目描述
    给定一个单词S和一个文本C。返回该单词在文本中的字谜出现的次数。
"""
"""
输入描述
    输入的第一行包含一个整数T，它表示测试用例的数量。 T测试用例的描述如下。
    每个测试用例的第一行包含仅包含小写字符的文本S。 
    第二行包含一个仅包含小写字母的单词。
    1 <= T <= 50
    1 <= |S| <= |C| <= 50
"""
"""
输出描述
    打印文本S中单词C的出现的次数（顺序可以不同）。
"""
times = int(input())
while times > 0:
    times = times - 1
    text = input()
    word = sorted(list(input()))
    answer = 0
    length = len(word)
    sets = []
    for i in range(length, len(text) + 1):
        sets = sets + [sorted(list(text[i - length: i]))]
    for j in sets:
        if j == word:
            answer = answer + 1
    print(answer)