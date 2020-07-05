arr=list(eval(input()))
fir=0
sec=0
thi=0
tmp=0
for i in range(len(arr)):
    if int(arr[i])>fir :
        tmp=i
        fir=int(arr[i])
arr[tmp]=arr[len(arr)-1]
for i in range(len(arr)-1):
    if int(arr[i])>sec :
        tmp=i
        sec=int(arr[i])
arr[tmp]=arr[len(arr)-2]
for i in range(len(arr)-2):
    if int(arr[i])>thi :
        tmp=i
        thi=int(arr[i])
print(str(fir*sec*thi))