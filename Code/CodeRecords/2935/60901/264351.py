def cntA(list, begin, end):
    numA = 0
    for i in range(begin,end):
        if list[i] == 'A':
            numA += 1
    return numA

def question6():
    l = list(input())
    total = 0
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i] == 'Q' and l[j] == 'Q':
                total += cntA(list=l, begin=i, end=j)
    return total
    
if __name__ == '__main__':
    print(question6(),end = '')