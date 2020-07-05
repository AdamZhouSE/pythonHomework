n=int(input())
s=[]
for i in range(n):
    arrayString=input()
    array=eval(arrayString)
    s+=array
k=int(input())
s.sort()
print(s[k-1])
   