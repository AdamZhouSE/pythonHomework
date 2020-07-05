import itertools
def main():
    numOftests = int(input())
    for i in range(numOftests):
        n = int(input())
        list0 = list(map(int,input().split()))
        k = int(input())
        list1 = list(itertools.combinations(list0,2))
        cnt = 0
        #print(list1)
        list2 = remov(list1)
        #print(list2)
        for x in list2:
            if abs(x[1]-x[0])==k:
                cnt+=1
        print(cnt)

def remov(list1):
    for j in range(len(list1) - 1):
        for k in range(j + 1, len(list1)):
            if (list1[j][0] == list1[k][1] and list1[j][1] == list1[k][0]) or (list1[j][0] == list1[k][0] and list1[j][1] == list1[k][1]):
                list1.pop(k)
                return remov(list1)
    return list1

if __name__ == '__main__':
    main()