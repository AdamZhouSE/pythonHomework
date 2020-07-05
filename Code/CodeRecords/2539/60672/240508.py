import copy
ar=input()
br=copy.copy(ar)
ar.sort()
start=0
end=len(ar)-1
for i in range(len(ar)):
    if br[i]==ar[i]:
        start=start+1
    else:
        break
for j in range(len(ar)):
    if br[len(ar)-1-j]==ar[len(ar)-1-j]:
        end=end-1
    else:
        break
con=end-start+1
print(con)