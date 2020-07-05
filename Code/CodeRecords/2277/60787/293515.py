k=int(input())
n=int(input())
count=0
start=1
end=n
while start<end-1:
    end=(start+end)//2
    count+=1
print(count+1)