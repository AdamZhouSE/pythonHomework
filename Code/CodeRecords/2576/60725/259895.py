arrayString=input()
target=int(input())
array=eval(arrayString)
q=len(array)
n=int(target/q)
m=min(array)
if m>n :
    print(n)
      
           