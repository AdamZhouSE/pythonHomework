def swap(lst,i,j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def eo_sort(lst):
    index_e = 0 #even index
    index_o = 1 #odd index
    n = len(lst)
    while 1:
        while index_e < n and lst[index_e]%2 == 0:
            index_e = index_e + 2
        while index_o < n and lst[index_o]%2 == 1:
            index_o = index_o + 2
        if index_o >= n or index_e >= n:
            break
        swap(lst,index_e,index_o)
        index_e = index_e + 2
        index_o = index_o + 2

if __name__ == "__main__":
    lst = eval(input())
    eo_sort(lst)
    print(lst)