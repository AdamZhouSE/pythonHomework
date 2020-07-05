intervals=eval(input())
intervals.sort(key=lambda x:x[0])
merged=[]
while len(intervals)>0:
    a=intervals.pop(0)
    while len(intervals)>0 and intervals[0][0]<=a[1]:
        b=intervals.pop(0)
        a[1]=max(a[1],b[1])
    merged.append(a)
print(merged)