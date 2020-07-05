def main():
    T=int(input())
    container=[]
    while T>0:
        T-=1
        N = int(input())
        arr = list(map(int, input().split(" ")))
        container.append(arr)
    for arr in container:
        mularray(arr)



def mularray(arr):
    result=[]
    for i in range(0, len(arr)):
        mul=1
        for j in range(0, len(arr)):
            if i!=j:
                mul=mul*arr[j]
        result.append(mul)
    for ele in result:
        print(ele, " ")
    print()
    
if __name__=='__main__':
    main()