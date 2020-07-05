def h_3_6():
    n = int(input())
    arr = list(map(int,input().split()))
    sum_Saraga = 0
    sum_Diga = 0
    i = 1
    while(len(arr)>0):
        if(arr[0]>arr[len(arr)-1]):
            c = arr[0]
            arr.remove(arr[0])
        else:
            c = arr[len(arr)-1]
            arr.remove(arr[len(arr)-1])
        if(i%2==1):
            sum_Saraga+=c
        else:
            sum_Diga+=c
        i+=1
    print(sum_Saraga,end=" ")
    print(sum_Diga)

if __name__ == '__main__':
    h_3_6()