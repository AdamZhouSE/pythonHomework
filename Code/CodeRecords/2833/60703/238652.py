n=int(input());
Str1 = input().split();
Str2 = input().split();
list1=[];
list2=[];
num=0;
for i in range(0,n):
    list1.append(int(Str1[i]));
    list2.append(int(Str2[i]));
    num=num+int(Str1[i]);
list2.sort(reverse=True);
if(list2[0]+list2[1]>=num):
    print("YES");
else:
    print("NO");
