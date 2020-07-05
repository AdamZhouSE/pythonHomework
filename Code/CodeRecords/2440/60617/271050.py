def insert_Sort():
    arr=eval(input())
    link=[]
    for ele in arr:
        if not link:
            link.append(ele)
        else:
            for i in range(0, len(link)):
                if ele>=link[len(link)-i-1]:
                    link.insert(len(link)-i, ele)
                    break
                elif i!=len(link)-1:
                    continue
                else:
                    link.insert(0,ele)

    print(link)

if __name__=='__main__':
    insert_Sort()