def main():
    numOftests = int(input())
    for i in range(numOftests):
        length = int(input())
        list0 = list(map(int, input().split()))
        list0 = pe(list0)
        list3 = list(map(str, list0))
        str1 = ' '.join(list3)
        print(str1 )


def pe(list0=''):
    for j in range(len(list0) - 1):
        if list0[j] == list0[j + 1] and list0[j]!= 0:
            list0[j] *= 2
            list0[j + 1] = 0
    numOfzero = list0.count(0)
    for i in range(numOfzero):
        list0.remove(0)
    for i in range(numOfzero):
        list0.append(0)
    return list0

if __name__ == '__main__':
    main()