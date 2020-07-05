num=int(input())
arr=[int(n) for n in input().split(' ')]
if num==1:
    if arr[0]==0:
        print('UP')
    else:
        print(-1)
else:
    mark=1
    for i in range(1,num):
      if  arr[i]>arr[i-1]:
          continue
      else:
          mark=0
          break
    if mark==1:
        if arr[num-1]==15:
            print('DOWN')
        else:
            print('UP')
    else:
        if arr[num-1]==0:
            print('UP')
        else:
            print('DOWN')