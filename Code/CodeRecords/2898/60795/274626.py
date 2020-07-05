n=int(input())
bit=input()
index,mark=1,0
if bit[0]=='0':
    mark=1
while True:
    if index<len(bit):
       if bit[index]=='1':
          arr=list(bit)
          arr[index]='0'
          if mark==1:
              arr[0]='1'
              bit="".join(arr)
              mark=0
          else:
              bit="".join(arr)
              bit="1"+bit[2:]
          index=1
       else:
           index+=1
    else:
        break

print(bit)