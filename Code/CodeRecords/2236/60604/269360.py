def ins(arr,a):
    arr.append(a)
    arr.sort()
    return arr
def de(arr,a):
    for i in range(len(arr)):
        if arr[i]==a:
            arr.remove(i)
            return arr


n=int(input())
a=[]
for I in range(n):
    x=input().split()
   # print(x)
    if int(x[0])==1:
        a=ins(a,int(x[1]))
    elif int(x[0])==2:
        a.remove(int(x[1]))
    elif int(x[0])==3:
        for i in range(len(a)):
            if a[i]==int(x[1]):
                print(i+1)
                break
    elif int(x[0])==4:
        print(a[int(x[1])-1])
    elif int(x[0])==5:
        tmp=0
        for i in a:
            if i<int(x[1]) and i>tmp:
                tmp=i
        print(tmp)
    elif int(x[0])==6:
        tmp=100000000000000000
        for i in a:
            if i>int(x[1]) and i<tmp:
                tmp=i
        print(tmp)
  #  print(a)
