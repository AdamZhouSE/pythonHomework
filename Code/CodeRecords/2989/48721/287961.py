a=input();
b=input();
c=input();
if(a<b):
    if(a<c):
        print(a);
        if(b<c):
            print(b);
            print(c);
        if(b>=c):
            print(c);
            print(b);
    if(a>=c):
        print(c);
        print(a);
        print(b);
if(b<=a):
    if(b<c):
        print(b);
        if(a<c):
            print(a);
            print(c);
        if(a>=c):
            print(c);
            print(a);
    if(b>=c):
        print(c);
        print(b);
        print(a);
        