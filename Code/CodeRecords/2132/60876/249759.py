string=list(input())
alpha=["zero","one","two","three","four","five","six","seven","eight","nine"]
length=len(string)
for item in alpha:
    jud=True
    while jud:
        for items in list(item):
            if not items in string:
                jud = False
                break
        if jud:
            for items in list(item):
                del string[string.index(items)]
            print(alpha.index(item), end="")
print()