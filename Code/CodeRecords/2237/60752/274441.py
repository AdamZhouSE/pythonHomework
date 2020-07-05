i1=input().split()
lst=[i for i in range(1,int(i1[0])+1)]
for i in range(int(i1[1])):
    ii=list(map(int,input().split()))
    start=ii[0]-1
    end=ii[1]
    clip=lst[start:end]
    clip.reverse()
    lst=lst[0:start]+clip+lst[end:]
print(' '.join(map(str,lst)),end=' ')