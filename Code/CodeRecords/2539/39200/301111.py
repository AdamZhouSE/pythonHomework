string = input()
A = string[1:-1:1].split(",")
B = []
for C in A:
    B.append(int(C))
index = 0
start = 0
end = 0
while(index<len(B)-1):
    if B[index]>B[index+1]:
        start = index
        break
    index = index + 1
index = len(B)-1
while(index>0):
    if B[index]<B[index-1]:
        end = index
        break
    index = index - 1
print(end-start+1)
