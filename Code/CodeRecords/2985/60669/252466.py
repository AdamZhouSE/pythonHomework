n=int(input())
result="A"

for i in range(1,n):
    temp="".join(reversed(result))
    temp=chr(65+i)+temp
    result+=temp
print(result)
