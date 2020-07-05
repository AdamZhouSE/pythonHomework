def question34():
    l = list(map(int, input().strip('[').strip(']').split(',')))
    k = int(input())
    lst = []
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            lst.append(abs(l[i] - l[j]))
    sub = list(set(lst))
    sub.sort()
    return sub[k-1]

if __name__ == '__main__':
    print(question34())