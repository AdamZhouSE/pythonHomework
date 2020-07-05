def partial_sort():
    row1st=input().split(" ")
    n=int(row1st[0])
    m=int(row1st[1])
    arr=list(map(int, input().split(" ")))
    sort_list=[]
    for i in range(0, m):
        sort_list.append(list(map(int, input().split(" "))))
    q=int(input())
    for ele in sort_list:
        reverse=ele[0]
        start=ele[1]-1
        end=ele[2]
        if reverse==0:
            part_sorted=sorted(arr[start:end])
        else:
            part_sorted=sorted(arr[start:end], reverse=True)
        arr[start:end]=part_sorted
    print(arr[q-1])        

if __name__=='__main__':
    partial_sort()