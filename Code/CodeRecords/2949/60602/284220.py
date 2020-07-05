def reverseNum(list):
    list.reverse();
    i=1;
    while(i<len(list)-1):
        print(list[i],end=" ");
        i+=1;
    print(list[len(list)-1],end="");

list=input().split(" ");
reverseNum(list);