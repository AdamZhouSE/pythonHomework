left=int(input())
right=int(input())
list=[]
for i in range(left,right+1):
    th,hu,de,fa=0,0,0,0
    if i<10:
        list.append(i)
    elif i>10&i<100:
        de=i/10
        fa=i%10
        if fa>0:
           if i%de==0:
              if i%fa==0:
                 list.append(i)
    elif i>100&i<1000:
        hu=i/100
        de=i%100/10
        fa=i%100%10
        if hu>0&de>0&fa>0:
            if i%hu==0&i%de==0&i%fa==0:
                list.append(i)
    elif i>1000&i<10000:
        th=i/1000
        hu=i%1000/100
        de=i%1000%100/10
        fa=i%1000%100%10
        if th>0&hu>0&de>0&fa>0:
            if i%th==0&i%hu==0&i%de==0&i%fa==0:
                list.append(i)

print(list)

