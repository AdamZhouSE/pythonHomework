def swap(x,y,arr):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

def filter(point,array):
    point -= 2
    while point >= 0:
        if array[point] <= array[point+2]:
            break
        swap(point,point+2,array)
        point -= 2
        
def adjust(point,array):
    if array[point]%2 != point%2:
        i = point + 1
        while i < len(array):
            if array[i]%2 != i%2:
                swap(point,i,array)
                break
            i += 2
    
array = eval(input())
point = 0
while point < len(array)/2:
    adjust(point*2,array)
    adjust(point*2+1,array)
    filter(point*2,array)
    filter(point*2+1,array)
    point += 1
print(array)