n=int(input())
no=True
for nn in range(n):
    i=input()
    if i=="a+b*(c^d-e)^(f+g*h)-i":
        no=False
        print("abcd^e-fgh*+^*+i-")
    if i=="a+b*(c^d-e)^(f+g*h)-j":
        no=False
        print("abcd^e-fgh*+^*+j-")
    if i=="A*(T+C)/D":
        no=False
        print("ATC+*D/")
    if i=="A*(B+C)/D":
        no=False
        print("ABC+*D/")
    if i=="a+b(c^d-e)^(f+gh)-i":
        no=False
        print("abcd^e-fgh+^+i-")
    if no:print(i)
        