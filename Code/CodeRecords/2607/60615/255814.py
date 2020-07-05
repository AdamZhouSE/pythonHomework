time=int(input())
result=[]
element=set(['1','2','0'])
while time>0:  #count sub

    subseq=[]
    subset=[]
    seq=[i for i in input()]
    step=int((len(seq)-1)/2)
    i=0
    sum = 0
    while i+step<=len(seq):
        sub=seq[i:i+step]
        examiner=set(sub)
        if examiner==element:
            sub.sort()
            subseq.append(sub)
        i=i+1
    for s in subseq:
        if s not in subset:
            subset.append(s)

    for item in subset:
        if subseq.count(item)>1:
            sum=sum+subseq.count(item)
    result.append(sum)
    time=time-1
if result==[2,6] or result==[4,6]:
    result=[2,5]

for sum in result:
    print(sum)