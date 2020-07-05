arr=eval(input())
def heap(l):
    for i in range(l,-1,-1):
        sort(i,l)

def sort(i,l):
    if 2*i+1<=l:
        if 2*i+2>l:
            if arr[i]<arr[2*i+1]:
                arr[i],arr[2*i+1]=arr[2*i+1],arr[i]
        else:
            if arr[2*i+1]>=arr[2*i+2]:
                if arr[2*i+1]>arr[i]:
                    arr[i],arr[2*i+1]=arr[2*i+1],arr[i]
            else:
                if arr[2*i+2]>arr[i]:
                    arr[i],arr[2*i+2]=arr[2*i+2],arr[i]

for i in range(len(arr)-1,-1,-1):
    heap(i)
    arr[0],arr[i]=arr[i],arr[0]
print(arr)