NandM=input().split(" ")
N=int(NandM[0])
M=int(NandM[1])
str_array=[]
for t in range(N):
    str_array.append(input())
def search(str_array,begin,end):
    temp=sorted(str_array[begin-1:end])
    return temp[-1]
search_array=[]
for _ in range(M):
    search_array.append(list(map(int,input().split(" "))))
for t in search_array:
    print(search(str_array,t[0],t[1]))