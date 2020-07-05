list=input();
list.sort(key=None,reverse=False);

count=0;
length=len(list);
for i in range(length):
    sub=list[length-i-1]-list[length-i-2];
    add=list[length-i-1]+list[length-(i+2)];

    for j in range(len(list)-i-2):
        if (list[len(list)-i-3-j]>sub) & (list[len(list)-i-3-j]<add):
            print(add+list[len(list)-i-3-j]);
            count=1;
            break;
    if (count==1):
        break;
if(count==0):
    print(0);
