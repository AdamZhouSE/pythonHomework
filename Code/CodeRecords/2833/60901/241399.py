def question10():
    num = int(input())
    a = map(int,input().split(' '))
    b = map(int,input().split(' '))
    bi = sorted(b)
    contains = bi[len(bi)-1] + bi[len(bi) - 2]
    if contains >= sum(a):
        return 'YES'
    else:
        return 'NO'
    
if __name__ == '__main__':
    print(question10())