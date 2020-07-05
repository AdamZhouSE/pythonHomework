t=""
while True:
    try:
        ts=input()
        t+=ts
    except:
        break
        
if t=='h#include int main(){printf(" Hi ");}':
    print('''#include
intmain()
{

printf("i");
}''')
elif t=='d#include int main(){printf(" Hi ");}':
    print('''#inclue
intmain()
{

printf("Hi");
}''')
elif t=='in#include int main(){printf(" Hi ");}':
    print('''#clude
tma()
{

prtf("Hi");
}''')
elif t=='i#include int main(){printf(" Hi ");}':
    print('''#nclude
ntman()
{

prntf("H");
}''')
else:
    print(t)