from collections import Counter
def solve(num):
    n = len(num)//3
    dic = Counter(num) #字典
    #print(dic)
    newNum = list(set(num))#集合
    result = []
    for i in newNum:
        if dic.get(i) > n:
            result.append(i)
    return result
if __name__ == '__main__':
    line = input()
    line = line[1:len(line) - 1]
    line = line.replace(',', ' ')
    #print(line)
    num = list(map(int, line.split()))
    #print(num)
    print(solve(num))