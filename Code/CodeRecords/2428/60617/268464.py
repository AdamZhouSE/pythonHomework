def even_odd_sort():
    T=int(input())
    for i in range(0, T):
        do_sort()

def do_sort():
    N=int(input())
    arr=list(map(int, input().split(" ")))
    odd=[]
    even=[]
    for ele in arr:
        if ele%2==0:
            even.append(ele)
        else:
            odd.append(ele)
    odd.sort(reverse=True)
    even.sort()
    res=odd.extend(even)
    for ele in res[0:N-1]:
        print(ele, end=" ")
    print(res[-1])
    
if __name__=='__main__':
    even_odd_sort()
    