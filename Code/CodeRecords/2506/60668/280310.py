def find_12_longest(list = []):
    re = []
    for i in range(len(list)):
        j = i
        co = list[i]
        con = 1
        while(j < len(list)):
            if(list[j] > co):
                co = list[j]
                con+=1
            j += 1
        re.append(con)
    print(max(re))
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    find_12_longest(list)