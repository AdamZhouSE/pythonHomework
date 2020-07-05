def insert_Sort():
    arr=eval(input())
    link=[]
    for ele in arr:
        if not link:
            link.append(ele)
        else:
            for i in range(0, len(link)):
                if i==len(link)-1:
                    link.insert(0, ele)
                if ele>=link[len(link)-i-1]:
                    link.insert(len(link)-i, ele)
                    break
                else:
                    continue

    print(link)

if __name__=='__main__':
    insert_Sort()