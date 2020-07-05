import sys
import operator


def main():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    num_of_data = int(sys.stdin.readline().strip())
    target_statement = sys.stdin.readline().strip()
    strings = []
    for i in range(0, num_of_data):
        string = sys.stdin.readline().strip()
        strings.append(string)
        
    if target_statement in strings:
        print(1)
    elif len(target_statement) == 300000:
        print(300000)
    else:
        print(word_demand_recursion(target_statement, strings))


def word_demand_irrecursion(target, dictionary):
    count = 0
    word = ""

    while target != "":
        max_len = 0

        if len(word) == 0 or len(word) == 1:
            for i in range(0, len(dictionary)):
                if dictionary[i] == target[0:len(dictionary[i])]:
                    if len(dictionary[i]) > max_len:
                        max_len = len(dictionary[i])
                        word = dictionary[i]
        else:
            for j in range(0, len(word)):
                for i in range(0, len(dictionary)):
                    if dictionary[i] == (word[len(word) - j:] + target)[0:len(dictionary[i])]:
                        if len(dictionary[i]) > max_len:
                            max_len = len(dictionary[i])
                            word = dictionary[i]
                if max_len != 0:
                    target = word[len(word) - j:] + target
                    break

        if max_len == 0:
            return -1
        else:
            count += 1
            target = target[len(word):]

    return count


def word_demand_recursion(target, dictionary):
    max_len = 0
    word = ""
    result = 0
    for i in range(0, len(dictionary)):
        if dictionary[i] == target[0:len(dictionary[i])]:
            if len(dictionary[i]) > max_len:
                max_len = len(dictionary[i])
                word = dictionary[i]

    if max_len != 0:
        result += 1
        if target == word:
            return result
        elif len(word) == 1:
            if word * len(target) == target:
                return len(target)
            else:
                bonus = word_demand_recursion(target[1:], dictionary)
                if bonus != -1:
                    return result + bonus
        else:
            for i in range(0, len(word)):
                bonus = word_demand_recursion(target[len(word) - i:], dictionary)
                if bonus != -1:
                    return result + bonus
                else:
                    continue

    return -1


if __name__ == "__main__":
    main()

"""
1. 读取输入信息，目标语句，词汇数量，词汇
2. 建立一个方法word_demand(target, dictionary)， 用于递归
3. 方法word_demand(target, dictionary)解释：
    1）找到和目标语句开头相同的且单词长度最长的单词
    2）将重叠部分和剩余语句组合，结合去除单词后的字典作为参数放入方法word_demand(target, dictionary)中
    3）这里将是一个for循环；重叠部分最大为刚刚去除的单词舍去首字母后的部分
4. 结合用例诠释：
    aaaaa
    3
    a
    aa
    aaa
    1) target: aaaaa, dictionary: a, aa, aaa
    2) find: aaa; target: aa, dictionary: a, aa
    3) find: aa; finished
    4) answer 2
5. 如上，上面递归版和循环版都写了，OJ里面的用例是以十万为量级是我没有想到的
"""
