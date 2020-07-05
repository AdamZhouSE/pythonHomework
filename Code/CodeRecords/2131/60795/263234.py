arr=[int(n) for n in input().split(',')]
number=0
for i in range(3,len(arr)+1):
    for j in range(0,len(arr)):
        if j+i<=len(arr):
            k,mark=j,0
            while k<i:
               if k+i-1<len(arr):
                  if arr[k+1]-arr[k]==arr[k+2]-arr[k+1]:
                      k=k+1
                  else:
                      mark=1
                      break
               else:
                   break
            if mark==0:
               number=number+1
        else:
            break
print(number)