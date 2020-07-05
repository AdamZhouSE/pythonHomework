intab = "aeiou"
outtab = "     "
trantab = str.maketrans(intab, outtab)
num=int(input());
for j in range(0,num):

    string = input();
    string=string.translate(trantab);

    count=[];
    for i in string:
        if(i.isalnum()):
            if i not in count:
                 count.append(i);
    if(len(count)%2==0):
        print("SHE!")
    else:
        print("HE!");